from cgi import test
from itertools import count
from urllib import response
import json
from ..utils.tokens import *
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..models import *
import random
# Create your views here.


def quiz(request):
    #Obtain properties of a question
    if(request.method == 'GET'):
        try: 
            token = request.headers["Authorization"]
        except Exception: 
            return JsonResponse({"status": 400})

        if verify_token(token):
            data = extrat_token_info(token)
            u_id = data["id"]
            q_list = []
            q_list = list(Question.objects.exclude(user__id=u_id).filter(state=2).values_list("id", flat=True))
            v_list = list(Vote.objects.filter(user__id=u_id).values_list("question__id", flat=True))
            q_list = [x for x in q_list if x not in v_list]
            if q_list:
                q_id = random.choice(q_list)
                response = {}
                response["question"] = Question.objects.values_list("body", flat=True).get(id=q_id)
                response["options"] = list(Option.objects.filter(question__id=q_id).values_list("body", "justification", "is_correct"))
                response["tag"] = Question.objects.values_list("tag__value", flat=True).get(id=q_id)
                response["accepted"] = Vote.objects.filter(question__id=q_id).filter(is_approved=True).count()
                response["rejected"] = Vote.objects.filter(question__id=q_id).filter(is_approved=False).count()
                response["id"] = q_id
                response["status"] = 200

                return JsonResponse(response)
            else:
                return JsonResponse({})
        else:
            return JsonResponse({"status": 400, "errors": "No quizzes available to review."})


def vote(request):
    if request.method == 'POST':
        try:
            token = request.headers["Authorization"]
        except Exception:
            return JsonResponse({"status": 400})

        if not verify_token(token):
            return JsonResponse({"status": 400, "errors": "invalid token"})

        data = extrat_token_info(token)
        u_id = data["id"]
        body = json.loads(request.body)

        temp_question = Question.objects.get(id=body['id'])
        v = Vote(user_id=u_id, is_approved=body['accepted'], justification=body['value'], question_id=body['id'])
        v.save()

        if Vote.objects.filter(question__id=body['id'], is_approved=True).count() == 3:
            temp_question.state = 4
            temp_question.save()
            creator = User.objects.get(id=temp_question.user.id)
            if Question.objects.filter(user__id=creator.id).count() == 3:
                creator.role = 2
                creator.save()
            return JsonResponse({"status": 200, "message": f"question {body['id']} has been approved"})

        if Vote.objects.filter(question__id=body['id'], is_approved=False).count() == 3:
            temp_question.state = 3
            temp_question.save()
            return JsonResponse({"status": 200, "message": f"question {body['id']} has been rejected"})

        return JsonResponse({"status": 200, "message": "vote has been saved"})

