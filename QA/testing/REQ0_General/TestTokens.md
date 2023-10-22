## Author:
    Jóni Pereira

# Test Scenario:
    Verify if all the functionalities related with tokens work correctly
    
# Actions to take:
    1 - Test write_token: create a variable (new_token) to save the encryptation of a dictionary with keys = {name, id}
    2 - Test verify_token: use a funtion in a real token (new_token) and in a dummy one (old or random) in order to attemp a decode
    3 - Test extrat_token_info: use a funtion in a real token (new_token) and in a dummy one (old or random) in order to obtain back a dictionary
    4 - Test extract_token: Through a Virtual Environment, test the extraction of a Request's token

    These functionalities were tested following the scripts available in tokens.md
    
# Expected Result:
    1 - The passed dictionary will be converted and printed as a JWT token
    2 - If the passed token is valid, it presents a success message; if it's not valid, it presents a non successful message
    3 - Using the passed JWT token, it should decrypts it into the form of a dictionary
    4 - A token originated from the HTTP request should be returned

    All four functions should work correctly

# Observed Result:
    The observed result was precisely the expected
    
# Success? 
    Yes!