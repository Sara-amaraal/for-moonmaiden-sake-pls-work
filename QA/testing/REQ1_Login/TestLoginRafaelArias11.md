#### TEST 1.1.1

## Author:
Rafael Arias

# Test Cenario:
Test Login Page

# Actions to take:
User types: 'justAUser1' on Login username box
User types: 'admin123' on Login password box
User clicks Login button

# Expected Result:
System redirects to '/' page with User logged in
    
# Observed Result:
System redirects to '/' page with User logged in

# OK? 
Yes

-----

#### TEST 1.1.2

## Author:
Rafael Arias

# Test Cenario:
Test Login Page

# Actions to take:
User types: 'justAUser1' on Login username box
User types: 'thisIsATest' on Login password box
User clicks Login button

# Expected Result:
System feedbacks: 'Invalid Credentials!'
    
# Observed Result:
System feedbacks: 'Invalid Credentials!'

# OK? 
Yes

----

#### TEST 1.1.3

## Author:
Rafael Arias

# Test Cenario:
Test Login Page

# Actions to take:
User types: 'ThisIsATest' on Login username box (User not registered)
User types: 'thisIsATest' on Login password box
User clicks Login button

# Expected Result:
System feedbacks: 'Invalid Credentials!'
    
# Observed Result:
System feedbacks: 'Invalid Credentials!'

# OK? 
Yes

----

#### TEST 1.1.4

## Author:
Rafael Arias

# Test Cenario:
Test Login Page

# Actions to take:
User types: '' on Login username box (User not registered)
User types: '' on Login password box
User clicks Login button

# Expected Result:
System feedbacks: 'Invalid Credentials!'
    
# Observed Result:
System feedbacks: 'Invalid Credentials!'

# OK? 
Yes