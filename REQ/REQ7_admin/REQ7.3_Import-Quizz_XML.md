# REQ7.3 - Admin: Import Quizzes as XML

- **PRIMARY ACTOR:** Admin

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** Reviewers

- **PRECONDITIONS:**
1. Admin is logged on
2. XML is aligned with guidelines

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Admin can import quizzes with XML

- **MAIN SUCESS SCENARIO:** 
1. Admin enters '/admin' page 
2. System shows page with 'Import' option
3. Admin selects one XML file from their machine
4. Admin clicks 'Import'
5. XML file information is submitted
6. System feedbacks: Quizzes Sucessfully Imported

- **EXTENSIONS/ALTERNATIVE PATHS:** None

3. (a) File is not on format XML
6. (a) System feedbacks: Invalid format 

3. (b) Precondition 'XML is aligned with guidelines' fails 
6. (b) System feedbacks: Can't read data from XML file

---

# Guidelines & Restrictions

- XML needs to be aligned with other PLs
