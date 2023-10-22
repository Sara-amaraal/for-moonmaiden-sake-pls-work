## Author

    Miguel Leopoldo

# Test Scenario

    Whether the ``login_required`` decorator is working as intended.

# Actions to take

    Requests to the different API endpoints with a valid authentication, invalid authentication and expired authentication
    should be made.

# Expected Result

    The requests with a valid authentication token should get access to the endpoint. All others must fail.

# Observed Result

    Found an error in ``extract_token`` from module ``backend\main\api\utils\tokens.py``. If the token has less than six characters an error occurs.
    Found another error that occurs when a request is made without the parameter ``id`` to the endpoint ``api/REQ5/get_test/``
    If no authentication token is passed, we get an error saying that the user is not logged in. Everything ok here.
    If an authentication token is passed, we get access to the endpoints. Everything ok here.
    Despite the endpoint working, there are alot of bugs. Needs fixing.

# Success?

    No
