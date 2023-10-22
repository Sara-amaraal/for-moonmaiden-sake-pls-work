"""
This module contains Django views for user registration and login, providing functionality for user authentication and token retrieval

The script consists of the following functions:
    - get_values(payload: dict, keys: List[str]): Used to extract information from the payload dictionary
    - register(request: HttpRequest): Register a new user and return an authentication token.
    - login(request: HttpRequest): Authenticate a user and return an authentication token.

Usage:
    - Import this module and call the 'register' and 'login' functions from your Django views.

"""

from django.http import HttpRequest, JsonResponse
from django.db.utils import IntegrityError
from typing import List
import bcrypt
from ..models import User
from ..utils import tokens, requests

# ------------------------------------------------------AUXILIARY FUNCTIONS---------------------------------------------------


def get_values(payload: dict, keys: List[str]):
    """HELPER FUNCTION
    Get certant values in a dictionary
    Used to extract payload information

    Args:
        payload (dict): dictionary to extrat the values
        keys (List[str]): name of the values to look in the dict

    Returns:
        _type_: the value of the key in the dict

    Yields:
        _type_: the value of the key in the dict
    """

    # if the numb of keys == 1 we have to return (not yield) to not give a generator
    if len(keys) == 1:
        return payload.get(keys[0], None)

    for i in keys:
        val = payload.get(i, None)
        yield val


# ------------------------------------------------------API METHODS---------------------------------------------------


def register(request: HttpRequest):
    """REGISTRATION

    Register a User in the database and retrieve a token for authentication.

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """

    # PROTECTIONS:
    # all params required in the payload
    needed_params = ["username", "password", "email"]

    # method is POST?

    # no, denied
    if request.method != "POST":
        return JsonResponse(
            {"status": 405, "log": f"Method ({request.method}) not alowed, only POST"}
        )

    # yes, proceed

    # is payload empty?
    payload = requests.extract_request_params(request)

    # yes, denied
    if payload == {}:
        return JsonResponse({"status": 500, "log": "empty / invalid body"})

    # no, proceed
    password: str
    name, password, email = get_values(payload, needed_params)

    # email is optional
    if email is None:
        email = ""

    # all parameters were given?
    if None in (name, password, email):
        not_found = filter(lambda x: payload.get(x, None) is None, needed_params)
        # no, denied
        return JsonResponse(
            {"status": 400, "log": f"Param(s) {', '.join(not_found)} not found"}
        )

    # yes, proceed

    # create user
    # hash the password with random salt
    new_password = bcrypt.hashpw(password.encode("u8"), bcrypt.gensalt())
    new_user = User(name=name, password=new_password.decode("u8"), email=email)

    try:
        new_user.save()
    except IntegrityError:
        # because we will have to get the user in order to then get the password,
        # two users cannot exist with the same username
        return JsonResponse({"status": 500, "log": "Username already exists"})

    # print(new_user.id)
    return JsonResponse(
        {"status": 200, "token": tokens.write_token({"id": new_user.id}).decode("u8")}
    )


def login(request: HttpRequest):
    """LOGIN

    Verify User credentials and retrieve a token for authentication.

    Args:
        request (HttpRequest): request

    Returns:
        _type_: None
    """

    # all params required in the payload
    needed_params = ["username", "password"]

    # method is PUT?

    # no, denied
    if request.method != "PUT":
        return JsonResponse(
            {"status": 405, "log": f"Method ({request.method}) not alowed, only PUT"}
        )

    # yes, proceed

    # is payload empty?
    payload = requests.extract_request_params(request)

    # yes, denied
    if payload == {}:
        return JsonResponse({"status": 500, "log": "empty / invalid body"})

    # no, proceed
    password: str
    username, password = get_values(payload, needed_params)

    # verify credentials in the db
    try:
        user = User.objects.get(name=username)

        if not bcrypt.checkpw(password.encode("u8"), user.password.encode("u8")):
            raise User.DoesNotExist  # to get the exeption below
    except User.DoesNotExist:
        # if username cannot be found or password is wrong
        return JsonResponse({"status": 500, "log": "Invalid credentials"})

    return JsonResponse(
        {"status": 200, "token": tokens.write_token({"id": user.id}).decode("u8")}
    )
