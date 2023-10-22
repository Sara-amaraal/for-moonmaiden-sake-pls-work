## Author

    Ana Rocha

# Test Scenario

    Test website URL navegation

# Actions to take

    Tried opening every page according to its route path (changing all the route paths to the URL link and seeing if it opens)

# Expected Result

    Every page should open according to its Route Path in the URL (for example an URL with '/login' should redirect the user to the login page)

# Observed Result

    The URL seems to work fine.
    The '/' route path should open the homepage. When u are not logged-in it redirects you to the login page instead and after you login it goes to the homepage.
    Even tho some pages are not possible to open (as in, it redirect you back to the homepage), it still works as it gives the user a reason. For example, the /review-quizz only opens when there are quizzes available to review, but it alerts the user and once there are quizzes available you can access the page fine.

# Success?

    Yes
