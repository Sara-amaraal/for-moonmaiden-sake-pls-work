# REQ1.3 - Logout

- **PRIMARY ACTOR:** User

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. User is logged in

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** User can logout

- **MAIN SUCESS SCENARIO:** 
1. User enters '/login' page (and is logged in)
2. System shows Login page and User is now logged out

- **EXTENSIONS/ALTERNATIVE PATHS:** None

# Guidelines & Restrictions

- None

---
### TESTS

### TEST 1.3.1
- Given: User is on any page (except '/login')
- When:
1. User clicks Logout button (turn off symbol)
- Then: System redirects to '/login' with User logged out