from cgi import test
from itertools import count
from urllib import response
import json
from ..utils.tokens import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..models import *
import random
from django.views.decorators.http import require_http_methods


def create_test(request):
    """Create a new test based on user-specified criteria and available questions.

    This view function allows users to create a new test with specific tags and a minimum of 20 questions.
    Questions are selected from the available pool of questions associated with the provided tags.

    Args:
        request (HttpRequest): The HTTP request object containing the user's request data.

    Returns:
        JsonResponse: A JSON response indicating the result of the test creation
    """

    # Extract the token from the request
    token = extract_token(request)

    if not verify_token(token):
        print(extrat_token_info(token))
        return JsonResponse({"status": 400, "errors": "invalid token"})

    user_id = extrat_token_info(token)["id"]
    # Loads the body from the request
    data = json.loads(request.body)

    tag_list = data["tags"]

    # Get the questions associated with each tag
    tag1 = list(Question.objects.filter(tag__value=tag_list[0]).exclude(
        num_tests__gt=1).filter(state=4))
    tag2 = list(Question.objects.filter(tag__value=tag_list[1]).exclude(
        num_tests__gt=1).filter(state=4))

    if len(tag1) == 0 and len(tag2) == 0:
        return JsonResponse({"status": 400, "errors": "No questions available."})

    # Ensuring that if we have more than 10 questions in each tag, we choose only 10 at random
    if len(tag1) > 10:
        tag1 = random.sample(tag1, 10)
    if len(tag2) > 10:
        tag2 = random.sample(tag2, 10)

    # This variable is used to keep track of how many question we still need in our test
    # A minimum of 20 questions is needed
    nr_remaining_questions = 20 - len(tag1) - len(tag2)

    # If it is above zero, it means we need more questions
    if nr_remaining_questions > 0:
        temp3 = Question.objects.exclude(num_tests__gt=1).filter(state=4).exclude(
            tag__value=tag_list[0]).exclude(tag__value=tag_list[1])[:nr_remaining_questions]
        tag2.extend(list(temp3))

    question_list = tag1 + tag2

    # If after adding more questions we still don't have 20, the test will not be created
    if len(question_list) < 20:
        return JsonResponse({"status": 400, "errors": "Not enough questions to make a test."})

    # Keep track of the number of questions with each unique tag
    tag_count = {}
    for question in question_list:
        try:
            tag_count[question.tag.value] += 1
        except KeyError:
            tag_count[question.tag.value] = 1

    # Create the test with the questions
    user = User.objects.get(id=user_id)
    new_test = Test(title=data["title"], creator=user)
    new_test.save()
    new_test.questions.add(*question_list)

    # Update the number of tests a question is in
    for question in question_list:
        question.num_tests += 1
        question.save()

    # Add tags to the test that exist within it's questions
    new_test.tags.add(Tag.objects.get(value=data["tags"][0]))
    new_test.tags.add(Tag.objects.get(value=data["tags"][1]))

    return JsonResponse({"status": 200, "message": "Test created successfully", "count": tag_count})


@require_http_methods(["GET"])
def tags(request):
    """Retrieve a list of all available tags.

    Args:
        request (HttpRequest): The HTTP request object containing the user's request data.

    Returns:
        JsonResponse: A JSON response containing the list of available tags.
    """

    # Extract the token from the request
    token = extract_token(request)

    if not verify_token(token):
        print(extrat_token_info(token))
        return JsonResponse({"status": 400, "errors": "invalid token"})

    # Get the list of tags
    tags = list(Tag.objects.all().values_list("value", flat=True))
    return JsonResponse({"status": 200, "tags": tags})
