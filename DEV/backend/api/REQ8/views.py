from django.http import HttpRequest, JsonResponse
from django.db.utils import IntegrityError

from ..models import User, Test, Question, Option, SolvedTest
from ..utils import tokens, requests


def get_username(request):
    """
     Returns a logged-in user's username or an error response.

     Args:
        request (HttpRequest): The HTTP request object representing the client request.

     Returns:
        JsonResponse: A JSON response containing the user's username or error.

     Raises:
        - 400 Bad Request if the request method is not GET.
        - 400 Bad Request with an error message if the user is not logged in or if the token is invalid.
        - 400 Bad Request with an error message if the user cannot be found.
     """

    if request.method != 'GET':
        return {"status": 400, "message": "wrong_request"}

    # Check if the user is logged in
    token = tokens.extract_token(request)

    if token is None or tokens.verify_token(token) is False:
        return JsonResponse({"error":
                             {"code": 400,
                              "message": "invalid_token: User is not logged in"
                              }})

    # Get the User from the token
    user_info = tokens.extrat_token_info(token)

    try:
        user = User.objects.get(pk=user_info.get("id"))
    except User.DoesNotExist:
        return JsonResponse({'status': 400,
                             'response': "could not find the user"
                             })

    # Return the username
    return JsonResponse({"status": 200, "username": user.name})


def get_stats_solver(request):
    """
    Returns a list of statistics for a Solver's performance on SolvedTest instances.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing statistics in the following format:
            {
                "status": 200,
                "data": [
                    {
                        "name": "Tag1",
                        "x": Number of correct answers for Tag1,
                        "y": Number of incorrect answers for Tag1
                    },
                    # Add more entries for other tags
                ]
            }

    Raises:
        - 400 Bad Request: If the request method is not GET.
        - 400 Bad Request: If the user's session token is invalid or the user is not logged in.
        - 400 Bad Request: If the user cannot be found.
        - 401 Unauthorized: If the user is not a Solver (user role is not 2).
    """

    if request.method != 'GET':
        return {"status": 400, "message": "wrong_request"}

    # Check if the user is logged in
    token = tokens.extract_token(request)

    if token is None or tokens.verify_token(token) is False:
        return JsonResponse({"error":
                             {"code": 400,
                              "message": "invalid_token: User is not logged in"
                              }})

    # Check if user is Solver
    user_info = tokens.extrat_token_info(token)
    user_id = user_info.get("id")

    try:
        user = User.objects.get(pk=user_info.get("id"))
    except User.DoesNotExist:
        return JsonResponse({'status': 400,
                             'response': "could not find the user"
                             })

    if user.role != 2:
        return JsonResponse({"status": 401,
                             'response': "user is not solver"
                             })

    stests = SolvedTest.objects.filter(user=user)

    response = {}
    for stest in stests:
        
        for opt in stest.options.all():
            tag_name = opt.question.tag.value
            if tag_name not in response:
                response[tag_name] = [0, 0]
            
            if opt.is_correct:
                response[tag_name][0] += 1
            else:
                response[tag_name][1] += 1
        
    data = []
    for i in response:
        data.append({
            "name": i,
            "x": response[i][0],
            "y": response[i][1],


        })

    # Returns: uniquetag:[TAG1,TAG2,....]
    #          percenta_aceite:[[%aceite_TAG1,%rejeitadoTAG1],
    #                           [%aceite_TAG2,%rejeitadoTAG2],...]
    return JsonResponse({'status': 200, "data": data})


def get_tags_creator(request):
    """
    Returns creator's tags.

    Retrieves and returns the tags created by a user who is a creator, along with the
    percentage of accepted and rejected questions associated with each tag.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing statistics in the following format:
            {
                "status": 200,
                "data": [
                    {
                        "name": "Tag1",
                        "x": Number of rejected questions for Tag1,
                        "y": Number of accepted questions for Tag1
                    },
                    # Add more entries for other tags
                ]
            }

    Raises:
        - 400 Bad Request: If the request method is not GET.
        - 400 Bad Request: If the user's session token is invalid or the user is not logged in.
        - 400 Bad Request: If the user cannot be found.
    """

    if request.method != 'GET':
        return {"status": 400, "message": "wrong_request"}

    # Check if the user is logged in
    token = tokens.extract_token(request)
    if token is None or tokens.verify_token(token) is False:
        return JsonResponse({"error":
                             {"code": 400,
                              "message": "invalid_token: User is not logged in"
                              }})

    # Check if user is a creator
    user_info = tokens.extrat_token_info(token)

    try:
        user1 = User.objects.get(pk=user_info.get("id"))
    except User.DoesNotExist:
        return JsonResponse({'status': 400,
                             'response': "could not find the user"
                             })

    unique_tags = []
    rescerta_reserrada = []
    question = Question.objects.filter(user=user1)
    response = {}
    # Take necessary information
    for squestion in question:
        if squestion.state not in (3, 4):
            continue
        tag_name = squestion.tag.value
        if tag_name not in response:
            response[tag_name] = [0, 0]
        
        if squestion.state == 3:
            response[tag_name][1] += 1
        if squestion.state == 4:
            response[tag_name][0] += 1

    # Put relevant information in arrays unique_tag and percentaaceite
    data = []
    for i in response:
        data.append({
            "name": i,
            "x": response[i][0],
            "y": response[i][1],


        })

    # Returns: uniquetag:[TAG1,TAG2,....]
    #          percenta_aceite:[[%aceite_TAG1,%rejeitadoTAG1],
    #                           [%aceite_TAG2,%rejeitadoTAG2],...]
    return JsonResponse({'status': 200, "data": data})
