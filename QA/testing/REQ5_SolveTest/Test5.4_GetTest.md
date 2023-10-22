## Author

    Miguel Leopoldo

# Test Scenario

    Whether the ``api/REQ5/get_test/`` endpoint is working as intended.

# Actions to take

    Requests to ``api/REQ5/get_test/`` will be made, using id's that are associated with a test, id's that aren't, and without id.

# Expected Result

    The requests should not return any test when the id is not associated with any test.
    The requests should return a test associated to the id if it exists.
    The requests should warn that there is no id when no id is passed as a parameter. 

# Observed Result

    The request is returning `Test not found` when the id is not associated with any test.
    The request is returning a test associated to the id when it exists.
    The request is throwing an error. It should be caught and treated.
    Despite the endpoint working, there are errors that must be fixed.

# Success?

    No
