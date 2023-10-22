## Author:
    Ana Rocha

# Test Cenario:
    Test if file import and export is working

# Actions to take:
    Comparing REQ7 with website, doing all possibilities and seing if everything works as expected.

# Expected Result:
    REQ7.1
    1. Admin enters '/admin' page
    2. System shows '/admin' page with Import and Export Quizzes options
    REQ7.3
    3. Admin enters '/admin' page
    4. System shows page with 'Export' option
    5. Admin clicks 'Export'
    6. XML file with all quizzes is created
    7. XML file with all quizzes is downloaded
    REQ7.3
    8. Admin enters '/admin' page
    9. System shows page with 'Import' option
    10. Admin selects one XML file from their machine
    11. Admin clicks 'Import'
    12. XML file information is submitted
    13. System feedbacks: Quizzes Sucessfully Imported

    (a) File is not on format XML
    (a) System feedbacks: Invalid format
    (b) Precondition 'XML is aligned with guidelines' fails
    (b) System feedbacks: Can't read data from XML file

# Observed Result:
    REQ7.1 and REQ7.2 work fine.
    
    On REQ7.3 no. 10, even when you try to input a file that is not XML (tried with a PDF file), no alert "File is not on format XML" or "System feedbacks: Invalid format" appears, instead it says "Quiz read sucessfully".

# OK? 
    No, problems with REQ7.3, mentioned above.