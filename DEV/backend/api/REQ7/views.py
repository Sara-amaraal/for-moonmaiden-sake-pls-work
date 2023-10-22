from django.http import HttpRequest, JsonResponse, HttpResponse
from typing import List, TextIO
from ..models import Question, Tag, Option, User
from ..utils import tokens

from pprint import pprint
import xmltodict

def load_info(request: HttpRequest):
    """
    View to load an XML file and create questions from it.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        JsonResponse: A JSON response with the status of the operation.
    """
    
    # Check if the HTTP method is POST (create).
    if request.method != "POST":
        return JsonResponse({'status': 405, 'log': f"Method ({request.method}) not allowed, only POST"})

    # Check user authentication.
    token = tokens.extract_token(request)
    if token is None:
        return JsonResponse({'status': 500, 'log': "User not logged in"})

    # Check token validation.
    token_info = tokens.extract_token_info(token)
    if token_info is None:
        return JsonResponse({'status': 500, 'log': "Expired session"})
    
    # Parse the uploaded XML file.
    file: TextIO = request.FILES['file']
    try:
        obj = xmltodict.parse(file.read().replace(b"A&D", b"AD"))
    except Exception as e:
        file.close()
        return JsonResponse({'status': 505, 'log': str(e)})
    file.close()

    # Check for the format of the XML in the 'perguntas' part.
    try:
        perguntas = obj['quizzess']['perguntas']['pergunta']
    except Exception:
        return JsonResponse({'status': 505, 'log': 'wrong format in perguntas'})
    del obj
    
    # Get the user to associate with the questions.
    user = User.objects.get(id=token_info['id'])
    
    # If there is only one 'pergunta,' it is saved as a dictionary and not a list (need to transform).
    if type(perguntas) == dict:
        perguntas = [perguntas]

    for pergunta in perguntas:
        # Create a question.
        temp_question = Question(user=user, body=pergunta['descricao'], state=2)

        # Check for the format of the XML in the 'tags' part.
        try:
            temp_tag_list = pergunta['tags']['tag']
        except Exception:
            return JsonResponse({'status': 505, 'log': 'wrong format in tags'})

        # If there is only one tag, it is saved as a string and not a list (need to transform).
        if type(temp_tag_list) == str:
            temp_tag_list = [temp_tag_list]

        # Associate the tags.
        for tag in temp_tag_list[:1]:
            if tag == "AD":
                tag = "A&D"
            try:
                temp_tag = Tag.objects.get(value=tag)
            except Tag.DoesNotExist:
                # If it doesn't find the tag, create it.
                temp_tag = Tag(value=tag)
                temp_tag.save()

            temp_question.tag = temp_tag
        
        temp_question.save()

        # Create the answers.
        if pergunta['respostas'] is None:
            continue

        temp_opts_list = pergunta['respostas']['resposta']
        if type(temp_opts_list) == dict:
            temp_opts_list = [temp_opts_list]
        
        for resp in temp_opts_list:
            if resp['justificacao'] is None:
                resp['justificacao'] = ""

            temp_resp = Option(
                question=temp_question,
                body=resp['designacao'],
                is_correct=resp['valor_logico'] == "True",
                justification=resp['justificacao']
            )
            temp_resp.save()

    return JsonResponse({"status": 200})

def send_info(request: HttpRequest):
    """
    View to send questions in XML format.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        HttpResponse: An HTTP response with an XML file.
    """
    
    # Check if the HTTP method is GET.
    if request.method != "GET":
        return JsonResponse({'status': 405, 'log': f"Method ({request.method}) not allowed, only GET"})

    # Check user authentication.
    token = tokens.extract_token(request)
    if token is None:
        return JsonResponse({'status': 500, 'log': "User not logged in"})

    # Check token validation.
    if not tokens.verify_token(token):
        return JsonResponse({'status': 500, 'log': "Expired session"})

    # Get 'json' format of questions    
    perguntas = []
    for i in Question.objects.exclude(state=1).exclude(state=3).all():
        temp_resposta = []
        for j in i.option_set.all():
            temp_resposta.append({
                'designacao': j.body,
                'justificacao': j.justification,
                'valor_logico': str(j.is_correct)
            })
        temp_pergunta = {
            'descricao': i.body,
            'tags': {'tag': [i.tag.value]},  # Only one mandatory tag
            'respostas': {'resposta': temp_resposta}
        }
        
        # Check if this question is equal to others.
        if any(temp_pergunta == j for j in perguntas):
            print("repeated")
            continue

        perguntas.append(temp_pergunta)
    
    # Create the XML response.
    resp = {'quizzess': {
        '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'perguntas': {'pergunta': perguntas}
    }}

    # Transform the dictionary into XML.
    temp = xmltodict.unparse(
        resp,
        pretty=True,  # Format with tabs and enters
        newl='\r\n'  # CRLF format
    ).replace("<tag>AD</tag>", "<tag>A&D</tag>")
        
    response = JsonResponse({'status': 200, 'data': temp})
    response['Content-Disposition'] = 'attachment'
    return response

def temp(request: HttpRequest):
    """
    A temporary view for testing purposes. Reads and parses an XML file.

    Args:
        request (HttpRequest): The HTTP request.

    Returns:
        JsonResponse: An empty JSON response.
    """
    
    with open("temp.xml", "r") as file:
        obj = xmltodict.parse(file.read())

    perguntas = obj['quizzess']['perguntas']['pergunta']
    del obj
    
    pprint(perguntas)

    return JsonResponse({})

