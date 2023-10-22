from django.http import JsonResponse, HttpRequest
from ..models import Test, SolvedTest, Option, User
from ..utils import tokens, requests
from django.db.utils import IntegrityError
from functools import wraps


# custom decorators
def check_method(method: str):
    """Decorator to restrict an endpoint to a specific HTTP request method.

    Args:
        method (str): The expected HTTP request method (e.g., 'GET', 'POST', 'PUT').

    Returns:
        callable: The decorated view function.
    """
    def inner(func):
        @wraps(func)
        def inner2(request: HttpRequest, *args, **kwargs):
            if request.method != method:
                return JsonResponse({
                    'status': 400,
                    'log': f'Method ({request.method}) not allowed, only {method}'
                })

            return func(request, *args, **kwargs)

        return inner2

    return inner


def login_required(token_var_name: str = None, *, verify_exp=True):
    """Decorator used for checking if the user is authenticated when accessing an endpoint.

    Args:
        token_var_name(str, optional): The name of the variable that will store the token payload. If provided, the decorator will attach the token payload to the view function's keyword arguments using this variable name. Defaults to None.
        verify_exp(bool, optional): If True, the decorator will verify the expiration of the user's token. Defaults to True.

    Raises:
        Exception: Raised if `token_var_name` is not a valid variable name.

    Returns:
        callable: The decorated view function.
    """
    debug_mode = False

    def inner(func):
        @wraps(func)
        def inner2(request: HttpRequest, *args, **kwargs):
            # check user auth
            token = tokens.extract_token(request)
            if token is None and not debug_mode:
                return JsonResponse({'status': 500, 'log': "User not logged in"})

            # if you dont need the payload
            if token_var_name is None and not debug_mode:
                if not tokens.verify_token(token, verify_exp=verify_exp):
                    return JsonResponse({'status': 500, 'log': "Expired session"})

                return func(request, *args, **kwargs)

            if not token_var_name.isidentifier():
                raise Exception(
                    f"\"{token_var_name}\" is not a valid var name!!!")

            # case you want token payload
            # check token validation
            token_payload = tokens.extrat_token_info(
                token, verify_exp=verify_exp)
            if token_payload is None and not debug_mode:
                return JsonResponse({'status': 500, 'log': "Expired session"})

            kwargs[token_var_name] = token_payload

            return func(request, *args, **kwargs)

        return inner2

    return inner


@check_method("GET")  # check if method is GET (get information)
@login_required()
def get_test(request: HttpRequest) -> JsonResponse:
    """Retrieve questions and options for a specific test.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the questions and options of the requested test.

    Raises:
        JsonResponse (status code 401): If the requested test does not exist.
    """
    payload = requests.extract_request_params(request)

    # Get the test from the database
    try:
        my_test = Test.objects.get(id=payload['id'])
    except Test.DoesNotExist:
        return JsonResponse({'status': 401, 'log': 'Test not found'})

    # Get questions information
    resp = []
    for question in my_test.questions.all():

        # Get the options from question
        temp_opts = []
        for opt in question.option_set.all():
            temp_opts.append({
                'id': opt.id,
                'body': opt.body
            })

        resp.append({
            'id': question.id,
            'body': question.body,
            'opts': temp_opts
        })

    return JsonResponse({'status': 200, 'questions': resp})


@check_method("GET")
@login_required("user_info")
def list_test(request: HttpRequest, user_info: dict):
    """View function for listing tests not yet solved by the authenticated user.

    Args:
        user_info (dict): A dictionary containing user information, retrieved from the user's access token.

    Returns:
        JsonResponse: A JSON response containing a list of tests that the user can attempt.
    """

    user_id = user_info.get("id")

    # get the tests already solved by the user
    solved_tests_ids = list(SolvedTest.objects
                            .filter(user__id=user_id)
                            .values_list('test__id', flat=True))

    # exclude the solved tests
    tests = Test.objects.all().exclude(pk__in=solved_tests_ids)

    response = []
    for test in tests:
        questions = test.questions.all()
        tags = list(questions.values_list('tag__value', flat=True).distinct())
        response.append({"id": test.id,
                         "title": test.title,
                         "tags": tags}
                        )

    return JsonResponse({"status": 200, "tests": response})


@check_method("POST")  # check if method is POST (create information)
@login_required("token_payload", verify_exp=False)
def grade_test(request: HttpRequest, token_payload: dict) -> JsonResponse:
    """Save the user's solutions for a test, calculate the grade, and provide justifications.

    Args:
        request (HttpRequest): The HTTP request object.
        token_payload (dict): The payload extracted from the user's access token.

    Returns:
        JsonResponse: A JSON response containing the grade and justifications for the user's selected options.

    Raises:
        JsonResponse (status code 501): If the user has already completed the same test.
    """

    req_payload = requests.extract_request_params(request)

    # get test and user
    my_test = Test.objects.get(id=req_payload['id'])
    user = User.objects.get(id=token_payload['id'])

    new_solved_test = SolvedTest(user=user, test=my_test)

    try:
        new_solved_test.save()
    except IntegrityError:
        # if there is a "SolvedTest" with the same user and test raises IntegrityError
        return JsonResponse({"status": 501, "log": "user already did this test"})
        # pass

    # get the chosen options of the user from the db
    my_opts = Option.objects.filter(
        id__in=map(str, list(req_payload['solutions'].values()))
    )

    # get the correct options of the questions of the test
    # [1] so quero as opts que estao corretas
    # [2] so quero as opts que pertencem a perguntas que pretencem ao "my_test"
    correct_opts = Option.objects.filter(is_correct=True)\
        .filter(question__in=my_test.questions.all())

    results = {}

    # init "results" with the correct answers
    for opt in correct_opts:
        results[opt.question.id] = {
            'justification': opt.justification,
            'correct': opt.id
        }

    grade = 0
    for opt in my_opts:
        new_solved_test.options.add(opt)  # relate opt to the SolvedTest

        grade += opt.is_correct  # grade += (True | False) = (1 | 0)

        # update "results" justification
        results[opt.question.id]['justification'] = opt.justification

    new_solved_test.grade = grade
    new_solved_test.save(force_update=True)  # update value

    return JsonResponse({'status': 200, 'grade': grade, "results": results})
