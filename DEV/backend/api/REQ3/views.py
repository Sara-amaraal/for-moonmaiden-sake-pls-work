import contextlib
from django.http import HttpRequest, JsonResponse
from django.db import transaction
from ..utils import tokens, requests
from ..models import User, Question, Option, Tag, Vote

# This flag allows to get the submited question on get_quiz function
debug = 1
invalid_token = "could not extract token info."
wrong_request = "wrong_request type"

def get_quiz(request: HttpRequest, question_id: int):
    
    """ Retrieves a draft or rejected quiz through its' id 
        and also the reviews if it's a rejected quiz
       
        Args:
            request(HttpRequest): request  
            question_id(int): id of the question
        
        Returns:
            JsonResponse: HttpResponse with the quiz information in JSON format
    """
    
    if request.method != "GET":
        return JsonResponse({"status": 404, "message": wrong_request})

    # Check if the user is logged
    token = tokens.extract_token(request)

    if not tokens.verify_token(token):
        return JsonResponse({"error": {"code": 400,"message": invalid_token}})

    # Extract information from token about user
    user_info = tokens.extrat_token_info(token)

    # Search for the saved question on database
    try:
        user = User.objects.get(pk = user_info.get("id"))
        question = Question.objects.get(pk = question_id, user = user)
        options = Option.objects.filter(question = question_id)
        
    except Question.DoesNotExist:
        return JsonResponse({"status": 404, "message": "quiz not found or the quiz is owned by another user"})
    except Exception as e:
        return JsonResponse({"status": 404, "message": str(e)}) 

    # Check if is editable
    if question.state != 1 and question.state != 3 and not debug: 
        return JsonResponse({"status": 401, "message": "quiz is not editable"})

    # Build the information dictionary
    data = {"question": question.body,
            "opt_text": question.opt_text,
            "tag": question.tag.value,
            "num_tests": question.num_tests
            }
    

    # If its a rejected quiz, add the reviews
    lista_justifications = []
    if question.state == 3:
        try:
            votes = Vote.objects.filter(question = question)
            lista_justifications.extend({"justification": vote.justification} for vote in votes)
        except Vote.DoesNotExist:
            pass
        except Exception:
            return JsonResponse({"status": 401, "message": "something wrong with the reviews"})
        
    data["rejected_justifications"] = lista_justifications

    #add the options
    lista_options = []
    with contextlib.suppress(Exception):
        lista_options.extend({"body": i.body, "is_correct": i.is_correct, "justification": i.justification} for i in options)

    data["options"] = lista_options

    return JsonResponse({"success": "true", "code": 201, "message": "information colected succesfully", "data": data})


def create_quiz(request: HttpRequest, state: int):
    """
        Saves or submits a quiz in the database
        Args:
            request(HttpRequest): request with the information about the quiz 
            state(int): the state of the quiz
        
        Returns:
            JsonResponse: HtppResponse with a validation of insert or update in database
    """

    # Check if it's a post
    if request.method != "POST":
        return JsonResponse({"status": 404, "message": wrong_request})

    # Check if the user is logged
    token = tokens.extract_token(request)

    if not tokens.verify_token(token):
        return JsonResponse({"status": 400,"message": invalid_token})

    # Extract information from token about user
    user_info = tokens.extrat_token_info(token)

    try:
        user = User.objects.get(id=user_info["id"])
    except User.DoesNotExist:
        return JsonResponse({"status": 400,"message": "User not found."})

    # Extract information from request
    payload = requests.extract_request_params(request)

    # Check if the question is already in the database
    if "question_id" not in payload:
        return JsonResponse({"status": 400,"message": "question_id not provided"})

    if payload["question_id"] <= 0:

        # It's a new question
        try:
            new_quiz(payload, user, state)
            return JsonResponse({"status": 201, "message": "Quiz submitted succesfully."})

        except Exception as e:
            return JsonResponse({"status": 400, "message": str(e)})

    else:
        try:
            # Get the quiz and update it
            quiz = Question.objects.get(id=payload["question_id"])
            tag = Tag.objects.get(value = payload["tag"]) 

            with transaction.atomic():
                update_quiz(payload, quiz, tag, state)
            return JsonResponse({"status": 201, "message": "Quiz submitted succesfully."})

        except Question.DoesNotExist:
            return JsonResponse({"status": 400, "message": "Quiz not found."})
        except Exception as e:
            return JsonResponse({"status": 400, "message": str(e)})


def update_quiz(payload, quiz, tag, state): 
    quiz.body = payload["body"]
    quiz.opt_text = payload["opt_text"]
    quiz.state = 2
    quiz.tag = tag
    quiz.num_tests = 0
    quiz.state = state
    quiz.save(update_fields=['body', 'opt_text', 'state', 'tag', 'num_tests'])

    # Delete all the previous options to avoid bugs and insert the new ones
    Option.objects.filter(question = quiz).delete()    

    # Delete votes to allow a new vote
    votes = Vote.objects.filter(question = quiz)
    votes.delete()

    for opt in payload["options"]:
            option = Option(question = quiz,
                            body = opt["body"],
                            is_correct = opt["is_correct"],
                            justification = opt["justification"]
                            )
            option.save()


def new_quiz(payload, user, state):
    tag = Tag.objects.get(value = payload["tag"])

    quiz = Question.objects.create(user=user,
                                   body=payload["body"],
                                   opt_text=payload["opt_text"],
                                   state=state,
                                   tag = tag
                                   )

    # Delete votes to allow a new vote
    votes = Vote.objects.filter(question = quiz)
    votes.delete()

    for opt in payload["options"]:
        Option.objects.create(question=quiz, body=opt["body"], is_correct=opt["is_correct"], justification=opt["justification"])


#TODO improve this view or remove it
def delete_quiz(request, question_id):
    
    """
        Delete a question and all the options with the id
        
        Args:
            request: dictionary to extrat the values 
            question_id: id of the question
        
        Returns:
            response: dictionary with a validation of insert or update in database
    """
    
    # Check if is a post
    if request.method != "POST":
        return JsonResponse({"status": 404, "message": "wrong request type"})
    
    # Check if the user is logged
    token = tokens.extract_token(request)

    if (tokens.verify_token(token)) == False:
        return JsonResponse({"error": {"code": 400,"message": invalid_token}})
    
    # Delete the question and the options
    try:
        quiz = Question.objects.get(id=question_id)
        options = Option.objects.filter(question=quiz.id)
        quiz.delete()

        for opt in options:
            opt.delete()

    except Exception as e:
        return JsonResponse({"error": {"code": 404, "message": str(e)}})

    return JsonResponse({"success": "true", "code": 200, "message": "Quiz deleted succesfully."})


""" 
SAVE E SUBMIT
{ 
    "question_id": 1,
    "body" : "teste",
    "opt_text": "texto opcional",
    "options" : [{"body":"option1", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option2", "is_correct": true, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option4", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"}
                ],
    "tag" :    "PM"
} 

GET
{ 
    "question": "teste",
    "opt_text": "texto opcional",
    "tag": "PM",
    "num_tests": 0,
    "rejected_justifications": [{"justification": "teste_rejeted_1"},
                                {"justification": "teste_rejeted_2"},
                                {"justification": "teste_rejeted_3"},
                                ]
    "options" : [{"body":"option1", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option2", "is_correct": true, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option4", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"},
                {"body":"option3", "is_correct": false, "justification":"alguma coisa"}
                ],
} 
"""
