#### TEST 1.2.1

## Author:
Rafael Arias

# Test Cenario:
Test Login Page

# Actions to take:
User types: 'myNewUser1' on Register username box
User types: 'password' on Register password box
User clicks Register button

# Expected Result:
System redirects to '/' page with User logged in
    
# Observed Result:
System redirects to '/' page with User logged in

# OK? 
Yes

----

#### TEST 1.2.2

## Author:
Rafael Arias

# Test Cenario:
Test Login Page

# Actions to take:
User types: 'justAUser1' on Register username box
User types: 'password' on Register password box
User clicks Register button

# Expected Result:
System feedbacks: 'Username already exists!'
    
# Observed Result:
System feedbacks: 'Username already exists!'

# OK? 
Yes

----

#### TEST 1.2.3

## Author:
Rafael Arias

# Test Cenario:
Test Login Page

# Actions to take:
User types: '' on Login username box (User not registered)
User types: 'password' on Login password box
User clicks Login button

# Expected Result:
System feedbacks: 'Username must be between 6 and 18 characters'
    
# Observed Result:
System feedbacks: 'Username must be between 6 and 18 characters'

# OK? 
Yes

----

#### TEST 1.2.4

## Author:
Rafael Arias

# Test Cenario:
Test Login Page

# Actions to take:
User types: 'myNewUser500' on Login username box (User not registered)
User types: '' on Login password box
User clicks Login button

# Expected Result:
System feedbacks: 'Password must be between 6 and 18 characters'
    
# Observed Result:
System feedbacks: 'Invalid Credentials'

# OK? 
No

