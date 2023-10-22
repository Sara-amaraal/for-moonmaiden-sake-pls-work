## Author

    Raquel Cardoso

# Test Scenario

    TEST 7.1: the system identifies when wrong type files are uploaded and imported by a website admin.
    TEST 7.1.1: the file uploaded is a pdf file containing scary type
    TEST 7.1.2: the file uploaded is a txt file containing xml code


    TEST 7.2: the system accepts right type files when uploaded and imported by a wbsite admin.
    TEST 7.2.1: the file uploaded is a xml file with acceptable code.
    TEST 7.2.2: the file uploaded is a xml file with random xml code.

    TEST 7.3: the system allows a website admin to export a file with the navigation links of the website.

# Actions to take

    TEST 7.1.1:The user must login with the admin credentials and access the '/admin/' page. Once there, the user must upload the given example of wrong type file 'scary_type_import_test.xml'. Finally, the user should click on the 'import' button.
    TEST 7.1.2: The user must login with the admin credentials and access the '/admin/' page. Once there, the user must upload the given example of a txt file 'good_type.txt'. Finally, the user should click on the 'import' button.

    TEST 7.2.1: The user must login with the admin credentials and access the '/admin/' page. Once there, the user must upload the given example of right type file 'good_type_import_tests.xml'. Finally, the user should click on the 'import' button.
    TEST 7.2.2: The user must login with the admin credentials and access the '/admin/' page. Once there, the user must upload the given example of right type wrong content file 'random.xml'. Finally, the user should click on the 'import' button.

    TEST 7.3: The user must login with the admin credentials and access the '/admin/' page. Once there, the user must click on the 'export' button.

# Expected Result

    TEST 7.1.1: It should appear an error message starting with "not well-formed".
    TEST 7.1.2: It should appear an error message starting with "not well-formed".

    TEST 7.2.1: It should appear an acceptance message saying "Quizzes read successfully!".
    TEST 7.2.2: It should appear an error message starting with "not well-formed".

    TEST 7.3: A xml file should be downloaded on the user's computer.

# Observed Result

    TEST 7.1.1: after trying to import the given file, the message shown was the one expected.
    TEST 7.1.2:after trying to import the given file, the message shown was the one expected.

    TEST 7.2.1: after trying to import the given file, the message shown was the one expected.
    TEST 7.2.2: after trying to import the given file, the message shown was the one expected.
    

    TEST 7.3: after clicking on the 'export' button, a xml file was downloaded. The file contained every navigation link of the website.

# Success?

    TEST 7.1.1: Yes
    TEST 7.1.2: Yes

    TEST 7.2.1: Yes
    TEST 7.2.2: Yes

    TEST 7.3: Yes

