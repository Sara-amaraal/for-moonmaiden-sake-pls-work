## Author

    Miguel Leopoldo

# Test Scenario

    Whether the ``api/REQ5/choose-test/`` endpoint is working as intended.

# Actions to take

    Requests to ``api/REQ5/choose-test/`` will be made, using a profile without completed tests and another with completed tests.

# Expected Result

    The requests made with the profile without completed tests should return every test.
    The requests made with the profile with completed tests should return every test except the ones already completed.

# Observed Result

    The request made with the profile without completed tests returned every test.
    The request made with the profile with completed tests returned every test except the ones already completed.
    This endpoint is working fine.

# Success?

    Yes
