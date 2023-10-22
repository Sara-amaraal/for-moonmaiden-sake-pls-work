"""
This file contains utility functions for extracting information from HTTP requests in a Django application.

Contents:
    - FakeRequest: A utility protected class created to simulate a fake HTTP request for testing purposes

The script consists of the following functions and classes:
    - __init__(self, method: str, body: bytes = b"", params: bytes = b"") -> None: FakeRequest protected class Constructor
    - extract_request_params(request: HttpRequest) -> Dict[str, Any]: Extracts information encoded in the request's body or parameters

"""
import sys, os
from django.http import HttpRequest
from typing import Any, Dict
import json
# Create a class for a fake request


# Tests working (no need to be applied anymore)
"""
# Navigate to project folder where main/settings.py is located
current_directory = os.path.dirname(os.path.realpath(__file__))
project_directory = os.path.abspath(os.path.join(current_directory, "../.."))
sys.path.append(project_directory)

# Set up Virtual Environment for testing
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
"""


# Create a class for a fake request
class _FakeRequest:
    def __init__(self, method: str, body: bytes = b"", params: bytes = b"") -> None:
        """
        Initialize a fake request object for extracting request parameters.

        Args:
            method (str): The HTTP method for the fake request
            body (bytes, optional): The request body as bytes (default is an empty bytes object)
            params (bytes, optional): The request parameters as bytes (default is an empty bytes object)

        Returns:
            _type_: None
        """
        self.method = method
        self.body = body
        self.params = params


def extract_request_params(request: HttpRequest) -> Dict[str, Any]:
    """
    Function to extract the information encoded in the request body or request parameters.

    Args:
        request (HttpRequest): The request from Django

    Returns:
        Dict[str, Any]: The extracted information in the form of a dictionary
    """

    if request.method == "GET":
        return request.GET

    if request.method in ("POST", "PUT"):
        if request.body == b"":
            return {}

        try:
            resp = json.loads(request.body)
        except SyntaxError:
            print(
                f"request.body with wrong format: b'{request.body.decode('u8')}'")
            return {}

        return resp

    return {}


"""
if __name__ == "__main__":
    try:
        # Create a sample HttpRequest instance
        request = HttpRequest()
        request.method = "GET"
        request.GET = {"param1": "value1", "param2": "value2"}

        # Call the extract_request_params function
        result = extract_request_params(request)
        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")
"""
