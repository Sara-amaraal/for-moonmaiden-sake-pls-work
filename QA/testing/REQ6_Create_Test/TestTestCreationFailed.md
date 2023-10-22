## Author
    Sofia Santos

#  Test Scenario
    Test the failure of a test creation.

#  Actions to take
    Log on the site, press the Create Test button. Create a test.

# Expected Result
    The system should show page with the title box, all 12 tags, Submit and Cancel options. Additionally, the user should only be able to select 2 tags. If the user fails to submit the test, the system should give feedback saying: Creation Failed. System should redirect to '/'. 

# Observed Result
    The system shows page with the title box, all 12 tags, Submit and Cancel options. The user can only select 2 tags, the sistem gives you a warning when you haven't selected 2 or when you select more. The cancel button also works, when you press it, it takes you to the home page. The submitt button also works showing all the necessary warnings. When the user does someting wrong when creating a teste the system doesn´t say 'Creation Failed' but gives other warnings. 

# Success? 
    Yes.