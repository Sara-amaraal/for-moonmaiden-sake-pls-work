## Author

    Raquel Cardoso

# Test Scenario

    Test if the hhtp paths received are being linked for the right method

# Actions to take

    Run the Backend app server and follow the given link. Once there, you should add paths to the website link starting with "/api/", then testing all the paths mentioned in the urls.py file: 
    - register/
    - login/
    - REQ2/
    - REQ3/
    - REQ4/
    - REQ5/
    - REQ6/
    - REQ7/
    - REQ8/

# Expected Result

    For each path, you should get a certain result:
    - register/ - an error message saying that only POST requests are allowed (this happens because we are only testing the path and not actually sending information as a POST request); 
    - login/ - similar to the one above, only instead the error mentions that only Put requests are allowed;
    - REQn/ -(n means the number of the request) more possible path should be presented, this means that we accessed the request urls file which contains different links for each method in each request. The paths shown should be different in each request as each one has different methods refering to different actions.
    

# Observed Result

    The results observed were exactly the ones described in the 'Expected Result' topic meaning the paths are working and the user is being linked for the right file/method.

# Success?

    Yes
