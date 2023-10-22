"""
Code respective to REQ2
"""

from django.http import JsonResponse, HttpRequest
# only works in scripts of the package, trying to run it with python interpreter will result in error
from ..models import User, Question, SolvedTest
from django.db.models import Count, Sum
# only works in scripts of the package, trying to run it with python interpreter will result in error
from ..utils.tokens import verify_token, extrat_token_info, extract_token

invalid_token = "could not extract token info."
wrong_request = "wrong request type."


def unfinished_reproved_quizzes(request: HttpRequest):
    """Returns all the quizzes that belong to the user

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """

    # Check if the method is a GET
    if request.method != 'GET':
        return {"status": 404, "message": wrong_request}

    # Check if the user is logged

    token = extract_token(request)

    if (verify_token(token)) == False:
        # not loggedin
        return JsonResponse({"error": {"code": 400, "message": invalid_token}})

    user_info = extrat_token_info(token)  # loggedin
    user_id = user_info.get("id")

    # Get quizzes
    response = list(Question.objects
                    .filter(user__id=user_id)
                    .values_list('id', 'state', 'tag__value', 'body'))

    return JsonResponse({'status': 200, 'unfinished_reproved_quizzes': response})


def solvers(request: HttpRequest):
    """Return all quiz solvers

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """
    # Check if the method is a GET
    if request.method != 'GET':
        return {"status": 404, "message": wrong_request}

     # Check if the user is logged in
    token = extract_token(request)

    if (verify_token(token)) == False:
        # not loggedin
        return JsonResponse({"error": {"code": 400, "message": invalid_token}})

    # Get solvers
    solvers = list(SolvedTest.objects
                   .values_list('user__name')
                   .annotate(score=Sum('grade'))
                   .order_by('-score')
                   [:10]
                   )

    return JsonResponse({'status': 200, 'solvers': solvers})


def creators(request: HttpRequest):
    """Returns all quiz creators

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """

    # Check if the method is a GET
    if request.method != 'GET':
        return {"status": 404, "message": wrong_request}

    # Check if the user is loggedin

    token = extract_token(request)

    if (verify_token(token)) == False:
        # not loggedin
        return JsonResponse({"error": {"code": 400, "message": invalid_token}})

    # Get creators
    creators = list(Question.objects
                    .filter(state=4)
                    .values_list('user__name')
                    .annotate(score=Count('user'))
                    .order_by('-score')
                    [:10]
                    )

    return JsonResponse({'status': 200, 'creators': creators})


def is_solver(request: HttpRequest):
    """Checks if the user is a solver

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """

    # Check if the method is a GET
    if request.method != 'GET':
        return {"status": 404, "message": wrong_request}

    # Check if the user is logged in
    token = extract_token(request)

    if (verify_token(token)) == False:
        # not loggedin
        return JsonResponse({"error": {"code": 400, "message": invalid_token}})

    user_info = extrat_token_info(token)
    user_id = user_info.get("id")  # get user id from token

    try:
        user = User.objects.get(id=user_id)  # get user id from the user table

    # check if user exists
    except User.DoesNotExist:
        # doesn't exist
        return JsonResponse({'status': 400, 'response': "could not find the user"})

    # response is the result from comparing the user role with 2 (int respective to the role of a solver in the database)
    response = user.role == 2

    return JsonResponse({'status': 200, 'response': response})
