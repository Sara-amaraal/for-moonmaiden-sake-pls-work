# REQ7.2 - Admin: Export Quizzes as XML

- **PRIMARY ACTOR:** Admin

- **SCOPE:** User Goals

- **STAKEHOLDER AND INTERESTS:** None

- **PRECONDITIONS:**
1. Admin is logged on
2. At least one Quizz to export 

- **MINIMAL GUARANTEE:** None

- **SUCESS GUARANTEE:** Admin can see '/admin' page

- **MAIN SUCESS SCENARIO:** 
1. Admin enters '/admin' page 
2. System shows page with 'Export' option
3. Admin clicks 'Export'
4. XML file with all quizzes is created
5. XML file with all quizzes is downloaded 

- **EXTENSIONS/ALTERNATIVE PATHS:**

4. (a) Precondition 'At least one Quizz to export' fails -> System feedbacks

---

# Guidelines & Restrictions

- XML needs to be aligned with other PLs
