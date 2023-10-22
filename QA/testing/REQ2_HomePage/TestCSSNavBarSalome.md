## Author:
    Salomé Monteiro

# Test Cenario:
    Testing the CSS on the website's nav bar

# Actions to take:
    Log In and navigate through the nav bar

# Expected Result:
    User can enter any page while seeing Navigation Bar with username and the current page is highlighted.

# Observed Result:
    It is possible to log in (with an existing account) and also register on the website if you don't have an account
    The user can enter any page in the nav bar and knowing in which page is currently on because it is highlighted by a darker color.

# OK? 
    Yes

### TESTS

### TEST 2.1.1
- Given: User is on any page (except '/login')
- When:
1. User clicks 'Create Quiz' button on NavBar 
- Then: System redirects to '/create-quizz' and 'Create Quiz' button on NavBar changes background to darker blue

Test 2.1.1 - Works

### TEST 2.2.1
- Given: User is on any page (except '/login')
- When:
1. User clicks 'Review Quiz' button on NavBar 
- Then: System redirects to '/review-quizz' and 'Review Quiz' button on NavBar changes background to darker blue

Test 2.2.1 - Works

### TEST 2.3.1
- Given: Solver is on any page (except '/login')
- When:
1. User clicks 'Solve Test' button on NavBar 
- Then: System redirects to '/choose-test' and 'Solve Test' button on NavBar changes background to darker blue

Test 2.3.1 - Works