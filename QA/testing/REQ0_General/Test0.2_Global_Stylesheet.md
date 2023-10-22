## Author:
    Catarina Araújo

# Test Cenario:
    Test the use of the classes used in the stylesheet.

# Actions to take:
    Check website elements that use specified classes.

# Expected Result:
    Specified classes correctly apply CSS properties (even if other CSS stylesheets overwrite them).

# Observed Result:
    The "root" pseudo-class is correctly applied.
    The "*" class is mostly always overwritten by higher spicificity classes from other stylesheets.
    The "box" class is mostly never overwritten and correctly applied.
    The "pergunta" is redundant in most cases, it is overwritten in most cases by other stylesheets.
    The "choice-container", "choice-prefix", "choice-text" and "correto" classes are hard to test as of the state of the Solve Test page.
    The remaining classes are correctly applied.

    In the Create Quizz page, class "pergunta" top-margin property's value and class "justificaco" width, height and bottom-margin property's values differ from applied values (other stylesheet classes).

    In the Create Test page, class "pergunta" top-margin property's value differs from applied value (other stylesheet class).

    In the Profile page, class "pergunta" margin-top and margin-left property's values differ from applied value (other stylesheet class -- margin: auto applied).

# OK? 
    OK