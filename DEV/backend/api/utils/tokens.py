"""
This file contains utility functions for working with JSON Web Tokens (JWT) and authentication in a Django application.

These functions are used for generating, verifying, and extracting information from JWTs.
They are designed to support secure user authentication and authorization.

Contents:
    - SECRET: A secret key used for JWT encoding and decoding (should be kept confidential to assure secure user authentication)

The script consists of the following functions:
    - write_token(data: dict) -> bytes: Generates a JWT with the provided data
    - verify_token(token: str, *, verify_exp=True) -> bool: Verifies the validity of a JWT
    - extract_token_info(token: str, *, verify_exp=True) -> dict | None: Extracts information stored in a JWT
    - extract_token(request: HttpRequest) -> str | None: Extracts an authentication token from an HTTP request

"""
import os
import sys
from datetime import datetime, timedelta
from jwt import encode, decode, exceptions
from django.http import HttpRequest

# Test 4 - working (no need to be applied anymore)
"""
#Navigate to project folder where main/settings.py is located
current_directory = os.path.dirname(os.path.realpath(__file__))
project_directory = os.path.abspath(os.path.join(current_directory, "../.."))
sys.path.append(project_directory)

# Set up Virtual Environment for testing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
"""

SECRET = "JrjvV*pV7j5lpY4Xf*CTo_vsn1U*mpikYGJ9FHWHsM&xXgMOAOj%Jd#5VslxUyUzEI4lOQUQNxB#oybe56VGFT%R5p8MEA7P#30VCsm6u&eUHryW#xVt5dJwZm?UHFtld3TVKxfMgNr5h#x5njj4SJjQYYJOqUwU1KGI9OUnuUUtxLE76o5JSdG7Nh4!aRrchWEQoTzG*Kgu1YKHXWdS0_J_v0nersuDki30Nofd5eLpBmwVu53vdFzQYifVUbUGS2L7e6Fz8jbFU?3F?Y%jEmbd#Dl&DefV*Pav4v%1?akD"


def write_token(data: dict) -> bytes:
    """
    Generate a JSON Web Token (JWT) with the provided data.

    Args:
        data (dict): Information to store in the token

    Returns:
        bytes: The token coded in bytes
    """

    # Duration of the token
    expier_date = lambda time: datetime.now() + timedelta(minutes=time)

    # Create token
    token = encode(
        payload={**data, "exp": expier_date(60)}, key=SECRET, algorithm="HS256"
    )
    return token.encode("UTF-8")


def verify_token(token: str, *, verify_exp=True) -> bool:
    """
    Verify if a token is valid.

    Args:
        token (str): The token to validate
        verify_exp (bool, optional): Flag to verify the token's expiration (default is True)

    Returns:
        bool: True if the token is valid, False otherwise
    """

    options = {"verify_exp": verify_exp}

    try:
        # If it runs with no problem means its valid
        decode(token, key=SECRET, algorithms=["HS256"], options=options)
    except exceptions.DecodeError:
        # In case we cannot decode

        return False
    except exceptions.ExpiredSignatureError:
        # In case the token validation has expired
        return False

    return True


def extrat_token_info(token: str, *, verify_exp=True) -> dict | None:
    """
    Extract the stored information from the token.

    Args:
        token (str): The token to extract information from
        verify_exp (bool, optional): Flag to verify the token's expiration (default is True)

    Returns:
        dict | None: A dictionary encoded within the token, or None if extraction fails
    """

    options = {"verify_exp": verify_exp}
    try:
        # If it runs with no problem means its valid
        return decode(token, key=SECRET, algorithms=["HS256"], options=options)

    except exceptions.DecodeError:
        # in case we cannot decode
        return None

    except exceptions.ExpiredSignatureError:
        # in case the token validation as expired
        return None


def extract_token(request: HttpRequest) -> str | None:
    """
    Extract the token from an HTTP request.

    Args:
        request (HttpRequest): The request from Django

    Returns:
        str | None: Returns the token if present, or None if it's not found in the request
    """
    token = request.headers.get("authorization", None)
    if token is None:
        return None

    if token[5] == " ":
        return token[6:]

    return token


def random_function(token: str):
    """
    Helper function to test token verification.

    Args:
        str: token to be verified

    Returns:
        _type_: None
    """
    if verify_token(token):
        print("Token is valid")
        # token is valid
    else:
        print("Token isn't valid")


"""
if __name__ == "__main__":
    try:
        # Testing write_token function
        new_token = write_token({"name": "Alberto", "id": 12})
        print(new_token)
        # WORKING!

        # Testing verify_token function
        random_function(new_token)
        random_function("random.token.testing")
        # WORKING!

        # Testing extrat_token_info function
        info = extrat_token_info(new_token)
        print(info)
        # WORKING!

        # Testing extracted_token function
        request = HttpRequest()
        request.META["HTTP_AUTHORIZATION"] = new_token
        extracted_token = extract_token(request)
        print("Result: ", extracted_token)
        # WORKING!

    except Exception as e:
        print(f"An error occurred: {e}")
"""
