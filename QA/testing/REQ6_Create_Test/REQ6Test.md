# Author

    Raquel Cardoso

## Test Scenario

    TEST 1: REQ6 URLs are giving the right path - backend
    TEST 1.1: When the path "test/" is received as an http request, the create_test method in the "views.py" file is called.
    TEST 1.2: When the path "tags/" is received as an http request, the tags method in "views.py" file is called.

    TEST 2: REQ6 URLs are giving the right path - backend and frontend - and the methods called are working properly.
    TEST 2.1: When in the path "/create-test" the "test/" is received and the create_test method in the "views.py" file is called
    TEST 2.2: When submitting a test the path "/tags" is received

    TEST 3: The methods create_test and tags are working properly, the tests are being created and saved in the databse.

## Actions to take

    TEST 1: The tester must initiate a backend test by opening the terminal and going to the DEV/backend directory. After making sure all the requirements are installed, the tester should run the comand  "python3 .\main\manage.py runserver" and open the given link. The path "/api/REQ6/" must be added to the current path of the page.
    TEST 1.1: The tester must add "test/" to the path as explained above.
    TEST 1.2: The tester must add "tags/" instead of "test/" to the path.

    TEST 2: The tester must initiate a backend test as described above. In another opened terminal, the tester should access the DEV/frontend directory. After making sure all the requirements are installed, the tester should run the comand " npm start". The tester should login using valid credentials.
    TEST 2.1: The tester must click on the "Create Test" button - the 4th button in the header bar. Once in the right page, the tester must write a name for the test and click on the "submit" button.
    TEST 2.2: The tester must click on the "Create Test" button - the 4th button in the header bar. Once in the right page, the tester must write a name for the test, click on two of the shown tags and click on the "submit" button.

    TEST 3: The tester must initiate a backend test as described above. In another opened terminal, the tester should access the DEV/frontend directory. After making sure all the requirements are installed, the tester should run the comand " npm start". The tester should login using valid credentials. The tester must click on the "Create Test" button - the 5th button in the header bar. Once in the right page, the tester must write a name for the test, click on two of the shown tags and click on the "submit" button. Lastly, the tester must click on the "Solve Test" button - 5th in the header bar - and confirm if there is any test with the name and tags like the one just created.

## Expected Result

    TEST 1.1 and TEST 1.2: An error message -" "status": 400,
    "errors": "invalid token" "- should appear as the tester is only testing the path and not actually sending a token, so the method is not receiving a token.

    TEST 2.1: An error message should appear saying the the teste must select 2 tags which means the name was accepted but the sent token was missing 2 tags. Also, in the terminal performing as server (the onde running the backend) the tester should be able to see a GET request which means the create_test method is working correctly.
    TEST 2.2: one of three scenarios can happen:
            2.2.1: A message saying "not enough questions to make a test" should appear meaning that there are not enough questions related to the selected tags in the database although the tags were successfully received.
            2.2.2: A message saying "No questions available" should appear meaning that there are no questions related to the chosen tags in the database although the tags were succeessfully received.
            2.2.3: A success message should appear showing the number of existing questions for each tag.

    TEST 3: It should appear a test with the same name and tags as the test created on the page, meaning it was actually created.

## Observed Result

    TEST 1.1: A message was obtained saying exactly what was expected.
    TEST 1.2: A message was obtained saying exactly what was expected.

    TEST 2.1: The results were the expected.
    TEST 2.2: 1st and 2nd- A success message was shown as described in the expected results 2.2.2.
              3rd - the "no questions available" message appeared.
              4th - a messagem saying "not enough quizzes to make a test" appeared.

    TEST 3: the tests created appeared on the "Solve Test" page.

## Success?

    TEST 1.1: Yes
    TEST 1.2: Yes

    TEST 2.1: Yes
    TEST 2.2: 1st, 2nd, 3rd - Yes
              4th - No

    TEST 3: Yes
