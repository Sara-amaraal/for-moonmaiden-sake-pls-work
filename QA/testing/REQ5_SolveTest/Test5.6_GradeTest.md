## Author

    Miguel Leopoldo

# Test Scenario

    Whether the ``api/REQ5/grade_test/`` endpoint is working as intended.

# Actions to take

    Requests to ``api/REQ5/grade_test/`` will be made without test id, with test id, without solutions, with wrong and right solutions and with a user that already completed that test.

# Expected Result

    The requests without test id should return some form of treated error.
    The requests with a test id but without solutions should return some form of treated error.
    The requests with a test id and solution should return a grade, as well as the answears to the input solutions.
    The requests with a test id but a user that already completed should return some form of treated error.

# Observed Result

    The requests without test id are returning an untreated error. Needs fixing.
    The requests without solutions are returning an untreated error. Needs fixing.
    The requests with solutions are returning a grade and the answears to the questions. Everything ok.
    The requests with a test id but a user that already completed it returns `user already did this test`. Everything ok.

# Success?

    No
