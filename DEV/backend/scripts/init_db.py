import bcrypt
from api.models import *
from api.REQ3.views import new_quiz

# run with python manage.py runscript init_db

def run():
    """
    Initializes the database with sample data.

    This script creates users, tags, and quizzes in the database.
    It also assigns roles and passwords to users using bcrypt for password hashing.

    Example:
    python manage.py runscript init_db
    """


    #create user1
    #warning security
    new_password = bcrypt.hashpw("admin123".encode('u8'), bcrypt.gensalt())
    new_user = User(name="justAUser1", password=new_password.decode('u8'), email="david@gmail.com",role=2)
    new_user.save()

    #create user2
    #warning security
    new_password = bcrypt.hashpw("admin123".encode('u8'), bcrypt.gensalt())
    new_user = User(name="justAUser2", password=new_password.decode('u8'), email="david@gmail.com",role=2)
    new_user.save()

    #create user3
    #warning security
    new_password = bcrypt.hashpw("admin123".encode('u8'), bcrypt.gensalt())
    new_user = User(name="justAUser3", password=new_password.decode('u8'), email="david@gmail.com",role=2)
    new_user.save()


    #create tags
    tags=["PM","REQ","A&D","IMP","TST","V&V","DEP","CI","PRC","PPL","CCM","RSK"]
    for tag in tags:
        new_tag=Tag(value=tag)
        new_tag.save()
    

    #create quizzes
    new_quiz({
        "tag":"PPL",
        "body":"The individual who uses the product after it has been fully developed and marketed is called:",
        "opt_text":"",
        "options":[
            {id:1,"body":"End User","is_correct":True,"justification":"1"},
            {id:2,"body":"Project manager","is_correct":False,"justification":"2"},
            {id:3,"body":"Programmer","is_correct":False,"justification":"3"},
            {id:4,"body":"Project Leader","is_correct":False,"justification":"4"},
            {id:5,"body":"Developer","is_correct":False,"justification":"5"},
            {id:6,"body":"Designer","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)

    new_quiz({
        "tag":"PRC",
        "body":"Which of the following follows the correct sequence in a waterfall model?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Testing, Design, Implementation, Feasibility, Requirements","is_correct":False,"justification":"1"},
            {id:2,"body":"Feasibility, Testing, Implementation, Requirement, Design","is_correct":False,"justification":"2"},
            {id:3,"body":"Testing, Design, Implementation, Feasibility, Requirements","is_correct":False,"justification":"3"},
            {id:4,"body":"Feasibility, Requirements, Design, Implementation, Testing","is_correct":True,"justification":"4"},
            {id:5,"body":"Testing, Implementation, Design, Feasibility, Requirements","is_correct":False,"justification":"5"},
            {id:6,"body":"Feasibility, Design, Requirements, Implementation, Testing","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)

    new_quiz({
        "tag":"PM",
        "body":"Which of each of the following is not an activity of the project planning process?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Draw up project schedule","is_correct":False,"justification":"1"},
            {id:2,"body":"Establish project constraints","is_correct":False,"justification":"2"},
            {id:3,"body":"Review project progress","is_correct":False,"justification":"3"},
            {id:4,"body":"Product reviews","is_correct":True,"justification":"4"},
            {id:5,"body":"All of the above","is_correct":False,"justification":"5"},
            {id:6,"body":"None of the above","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)

    new_quiz({
        "tag":"TST",
        "body":"A type of Software Life Cycle Activity which involves saving tests from the previous version to ensure that the new version retains the previous capabilities.",
        "opt_text":"",
        "options":[
            {id:1,"body":"Regression testing","is_correct":True,"justification":"1"},
            {id:2,"body":"Acceptance testing","is_correct":False,"justification":"2"},
            {id:3,"body":"Unit testing","is_correct":False,"justification":"3"},
            {id:4,"body":"System testing","is_correct":False,"justification":"4"},
            {id:5,"body":"Test-Driven Development","is_correct":False,"justification":"5"},
            {id:6,"body":"Testing","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"PM",
        "body":"Which deliverable document describes the order of tasks and estimates of time and effort necessary?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Source code","is_correct":False,"justification":"1"},
            {id:2,"body":"Software test plan","is_correct":False,"justification":"2"},
            {id:3,"body":"Lean Canvas","is_correct":False,"justification":"3"},
            {id:4,"body":"Database initialization script","is_correct":False,"justification":"4"},
            {id:5,"body":"Project schedule","is_correct":True,"justification":"5"},
            {id:6,"body":"None of the above","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"PM",
        "body":"Who is the person who has complete responsibility for the success of the project and has accountability to the stakeholders and sponsors.",
        "opt_text":"",
        "options":[
            {id:1,"body":"End User","is_correct":False,"justification":"1"},
            {id:2,"body":"Project Manager","is_correct":True,"justification":"2"},
            {id:3,"body":"Project Leader","is_correct":False,"justification":"3"},
            {id:4,"body":"Systems Analyst","is_correct":False,"justification":"4"},
            {id:5,"body":"CEO","is_correct":False,"justification":"5"},
            {id:6,"body":"Developer","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"PRC",
        "body":"Which of the following are examples of deliverable documents?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Defect report","is_correct":False,"justification":"1"},
            {id:2,"body":"Statement of work","is_correct":False,"justification":"2"},
            {id:3,"body":"User manual","is_correct":False,"justification":"3"},
            {id:4,"body":"Progress report","is_correct":False,"justification":"4"},
            {id:5,"body":"All of the answers","is_correct":True,"justification":"5"},
            {id:6,"body":"None of the above","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"REQ",
        "body":"CMMI stands for",
        "opt_text":"",
        "options":[
            {id:1,"body":"Capability Maturity Model Integrated","is_correct":True,"justification":"1"},
            {id:2,"body":"Critical Maturity Model Integrated","is_correct":False,"justification":"2"},
            {id:3,"body":"Critical Modeling Maturity Integrated","is_correct":False,"justification":"3"},
            {id:4,"body":"Capability Modeling Maturity Integrated","is_correct":False,"justification":"4"},
            {id:5,"body":"Capacity Modeling Maturity Integrated","is_correct":False,"justification":"5"},
            {id:6,"body":"Capacity Maturity Model Integrated","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"REQ",
        "body":"A type of Software Life Cycle Activity which involves updating and improving the software to ensure continued usefulness.",
        "opt_text":"",
        "options":[
            {id:1,"body":"Training","is_correct":False,"justification":"1"},
            {id:2,"body":"Maintenance","is_correct":True,"justification":"2"},
            {id:3,"body":"Installation","is_correct":False,"justification":"3"},
            {id:4,"body":"Delivery","is_correct":False,"justification":"4"},
            {id:5,"body":"Deployment","is_correct":False,"justification":"5"},
            {id:6,"body":"Presentation","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"CI",
        "body":"Which of the following lists the correct sequence of the five levels of the original CMM? (from the least mature to the most mature level)",
        "opt_text":"",
        "options":[
            {id:1,"body":"Initial, Repeatable, Managed, Defined, Optimizing","is_correct":False,"justification":"1"},
            {id:2,"body":"Optimizing, Managed, Defined, Repeatable, Initial","is_correct":False,"justification":"2"},
            {id:3,"body":"Initial, Managed, Repeatable, Defined, Optimizing","is_correct":False,"justification":"3"},
            {id:4,"body":"Initial, Repeatable, Defined, Managed, Optimizing","is_correct":True,"justification":"4"},
            {id:5,"body":"Initial, Optimizing, Repeatable, Defined, Managed","is_correct":False,"justification":"5"},
            {id:6,"body":"Optimizing, Managed, Repeatable, Initial, Defined","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)

    new_quiz({
        "tag":"IMP",
        "body":"A type of Software Life Cycle Activity which involves building the software and converting the design into code.",
        "opt_text":"",
        "options":[
            {id:1,"body":"Detailed design","is_correct":False,"justification":"1"},
            {id:2,"body":"Architectural design","is_correct":False,"justification":"2"},
            {id:3,"body":"Interface design","is_correct":False,"justification":"3"},
            {id:4,"body":"Deployment","is_correct":False,"justification":"4"},
            {id:5,"body":"Implementation","is_correct":True,"justification":"5"},
            {id:6,"body":"None of the above","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)
    
    new_quiz({
        "tag":"TST",
        "body":"In Test-Driven Development (TDD) what is a test?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Is when you use a concrete scenario and actual code.","is_correct":True,"justification":"1"},
            {id:2,"body":"Is where you use testing guidelines to choose test cases.","is_correct":False,"justification":"2"},
            {id:3,"body":"Is when a block of memory is shared between procedures or functions.","is_correct":False,"justification":"3"},
            {id:4,"body":"Is when you analyze the static system representation to discover problems.","is_correct":False,"justification":"4"},
            {id:5,"body":"Is when you manually test a feature.","is_correct":False,"justification":"5"},
            {id:6,"body":"Is when you fix a bug in the code.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)

    new_quiz({
        "tag":"PRC",
        "body":"Which of the following is not a phase of the software lifecycle in the Waterfall model?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Identify Risk.","is_correct":True,"justification":"1"},
            {id:2,"body":"Code/Implementation.","is_correct":False,"justification":"2"},
            {id:3,"body":"Operation.","is_correct":False,"justification":"3"},
            {id:4,"body":"Requirements.","is_correct":False,"justification":"4"},
            {id:5,"body":"Feasibility.","is_correct":False,"justification":"5"},
            {id:6,"body":"All above are phases of the software lifecycle in the Waterfall model.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"A&D",
        "body":"In the 4+1 views of software architecture what is the +1 refering to which view?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Development","is_correct":False,"justification":"1"},
            {id:2,"body":"Process","is_correct":False,"justification":"2"},
            {id:3,"body":"Use case","is_correct":True,"justification":"3"},
            {id:4,"body":"Physical","is_correct":False,"justification":"4"},
            {id:5,"body":"Implementation","is_correct":False,"justification":"5"},
            {id:6,"body":"Deployment","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"A&D",
        "body":"Which one of these affirmations about Architecture and Design is true?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Architecture is one specific solution in the multiple solutions space defined by the design.","is_correct":False,"justification":"1"},
            {id:2,"body":"Architecture is a design so all designs are an architecture.","is_correct":False,"justification":"2"},
            {id:3,"body":"Design is about the solution domain and is a very high level architecture focusing on main components.","is_correct":False,"justification":"3"},
            {id:4,"body":"Design is one specific solution in the multiple solutions space defined by the architecture.","is_correct":True,"justification":"4"},
            {id:5,"body":"All of the above.","is_correct":False,"justification":"5"},
            {id:6,"body":"None of the above.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"TST",
        "body":"Which of this options is not a Testing Stage:",
        "opt_text":"",
        "options":[
            {id:1,"body":"Acceptance testing","is_correct":True,"justification":"1"},
            {id:2,"body":"Development testing","is_correct":False,"justification":"2"},
            {id:3,"body":"Release testing","is_correct":False,"justification":"3"},
            {id:4,"body":"User testing","is_correct":False,"justification":"4"},
            {id:5,"body":"All of the above.","is_correct":False,"justification":"5"},
            {id:6,"body":"None of the above.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"PRC",
        "body":"Which are the RUP fases in order:",
        "opt_text":"",
        "options":[
            {id:1,"body":"Inception -> Elaboration -> Transition -> Construction","is_correct":False,"justification":"1"},
            {id:2,"body":"Inception -> Construction -> Elaboration -> Transition","is_correct":False,"justification":"2"},
            {id:3,"body":"Inception -> Elaboration -> Construction -> Transition","is_correct":True,"justification":"3"},
            {id:4,"body":"Inception -> Transition -> Elaboration -> Construction","is_correct":False,"justification":"4"},
            {id:5,"body":"Elaboration -> Inception -> Construction -> Transition","is_correct":False,"justification":"5"},
            {id:6,"body":"Elaboration -> Construction -> Inception -> Transition","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"PM",
        "body":"What are the four major phases of managing a software project?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Planning, Adjustment, Elaboration, Organization","is_correct":False,"justification":"1"},
            {id:2,"body":"Planning, Organization, Monitoring of status, Adjustment","is_correct":True,"justification":"2"},
            {id:3,"body":"Analysis, Organization, Monitoring of status, Development","is_correct":False,"justification":"3"},
            {id:4,"body":"Inception, Adjustment, Monitoring of status, Transition","is_correct":False,"justification":"4"},
            {id:5,"body":"Inception, Elaboration, Monitoring of status, Transition","is_correct":False,"justification":"5"},
            {id:6,"body":"Planning, Organization, Monitoring of status, Transition","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"REQ",
        "body":"Which of the following is false with regard to the spiral model of software development?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Each phase depends on the deliverables of the previous one and corresponds to a specialization of tasks.","is_correct":True,"justification":"1"},
            {id:2,"body":"It is an evolutionary model that includes an explicit risk analysis phase.","is_correct":False,"justification":"2"},
            {id:3,"body":"Spiral model is an incremental software development model.","is_correct":False,"justification":"3"},
            {id:4,"body":"Is used by software engineers and is favored for large, expensive and complicated projects.","is_correct":False,"justification":"4"},
            {id:5,"body":"All answers are False.","is_correct":False,"justification":"5"},
            {id:6,"body":"All answers are True.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)

    new_quiz({
        "tag":"V&V",
        "body":"Verification vs validation:",
        "opt_text":"",
        "options":[
            {id:1,"body":"Software verification tries to answer the question “Are we building the product right?”. Software validation tries to answer the question “Are we building the right product?”.","is_correct":True,"justification":"1"},
            {id:2,"body":"Software validation tries to answer the question “Are we building the product right?”. Software verification tries to answer the question “Are we building the right product?”.","is_correct":False,"justification":"2"},
            {id:3,"body":"Software verification tries to answer the question “Are we building the product right?“ and “Are we building the right product?”.","is_correct":False,"justification":"3"},
            {id:4,"body":"Software validation tries to answer the question “Are we building the product right?“ and “Are we building the right product?”.","is_correct":False,"justification":"4"},
            {id:5,"body":"Software verification and validation try to answer the question “Are we building the product right?“","is_correct":False,"justification":"5"},
            {id:6,"body":"Software verification and validation try to answer the question “Are we building the right product?“","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)
    
    new_quiz({
        "tag":"PM",
        "body":"The formal inspection process:",
        "opt_text":"",
        "options":[
            {id:1,"body":"Planning/Group Prep -> Individual Prep -> Review Meeting -> Error correction/Improvement -> Follow-up checks","is_correct":True,"justification":"1"},
            {id:2,"body":"Planning/Group Prep -> Follow-up checks -> Individual Prep -> Review Meeting -> Error correction/Improvement","is_correct":False,"justification":"2"},
            {id:3,"body":"Planning/Group Prep -> Individual Prep -> Error correction/Improvement -> Review Meeting -> Follow-up checks","is_correct":False,"justification":"3"},
            {id:4,"body":"Individual Prep -> Planning/Group Prep -> Review Meeting -> Error correction/Improvement -> Follow-up checks","is_correct":False,"justification":"4"},
            {id:5,"body":"Individual Prep -> Review Meeting -> Planning/Group Prep -> Error correction/Improvement -> Follow-up checks","is_correct":False,"justification":"5"},
            {id:6,"body":"Individual Prep -> Planning/Group Prep -> Error correction/Improvement -> Review Meeting -> Follow-up checks","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=1),4)

    new_quiz({
        "tag":"PM",
        "body":"Which one or which ones of this 4 is not a management fase in a software project:",
        "opt_text":"",
        "options":[
            {id:1,"body":"Planning","is_correct":False,"justification":"1"},
            {id:2,"body":"Monitoring of status","is_correct":False,"justification":"2"},
            {id:3,"body":"Adjustment","is_correct":False,"justification":"3"},
            {id:4,"body":"Adjustment and Planning","is_correct":False,"justification":"4"},
            {id:5,"body":"Planning and inception","is_correct":False,"justification":"5"},
            {id:6,"body":"Inception","is_correct":True,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"PM",
        "body":"What are the main criteria that determine the success of a software development project?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Fast development, Stable, Cost.","is_correct":False,"justification":"1"},
            {id:2,"body":"Cost, Schedule, Quality.","is_correct":True,"justification":"2"},
            {id:3,"body":"Quality, Stable, Cost.","is_correct":False,"justification":"3"},
            {id:4,"body":"Fast development, Stable, Schedule.","is_correct":False,"justification":"4"},
            {id:5,"body":"Fast development, Quality, Schedule.","is_correct":False,"justification":"5"},
            {id:6,"body":"Quality, Fast development, Cost.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"PRC",
        "body":"Choose the incorrect affirmation about ETVX:",
        "opt_text":"",
        "options":[
            {id:1,"body":"These operational definitions can then be adapted or tailored for use on all projects which uses the defined process architecture.","is_correct":False,"justification":"1"},
            {id:2,"body":"ETVX method is primarily for the description of activities, which are a set of tasks to be performed.","is_correct":False,"justification":"2"},
            {id:3,"body":"There are four phases, and they are Entry Criteria, Tasks to be performed, Exit Criteria and Validation, Verification Conditions for each task.","is_correct":False,"justification":"3"},
            {id:4,"body":"This is a method to depict the higher level or organizational level processes.","is_correct":True,"justification":"4"},
            {id:5,"body":"All of the above.","is_correct":False,"justification":"5"},
            {id:6,"body":"None of the above.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=2),4)

    new_quiz({
        "tag":"TST",
        "body":"At what stage of a software project should testing start?",
        "opt_text":"",
        "options":[
            {id:1,"body":"In Software Development Life Cycle (SDLC), testing can be started from the Requirements phase.","is_correct":True,"justification":"1"},
            {id:2,"body":"In Software Development Life Cycle (SDLC), testing can be started from the Analysis phase.","is_correct":False,"justification":"2"},
            {id:3,"body":"In Software Development Life Cycle (SDLC), testing can be started from the Coding/Implementation phase.","is_correct":False,"justification":"3"},
            {id:4,"body":"In Software Development Life Cycle (SDLC), testing can be started from the Design phase.","is_correct":False,"justification":"4"},
            {id:5,"body":"In Software Development Life Cycle (SDLC), testing can be started from the Operation/Deployment phase.","is_correct":False,"justification":"5"},
            {id:6,"body":"In Software Development Life Cycle (SDLC), testing can be started from the Maintenance phase.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"PRC",
        "body":"The Waterfall model (choose the incorrect):",
        "opt_text":"",
        "options":[
            {id:1,"body":"Incorporates a working version of the program from the beginning so that the client can provide feedback.","is_correct":True,"justification":"1"},
            {id:2,"body":"Has a Design phase.","is_correct":False,"justification":"2"},
            {id:3,"body":"Is suitable for projects with stable requirements.","is_correct":False,"justification":"3"},
            {id:4,"body":"Is characterized by a set of clearly defined milestones and deliverables.","is_correct":False,"justification":"4"},
            {id:5,"body":"Has a Coding/Implementation phase.","is_correct":False,"justification":"5"},
            {id:6,"body":"Is a sequential model for software development.","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"PPL",
        "body":"Six thinking hats; problem solving. What's the role of the red hat?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Used to obtain the positive outlook, this hat sees opportunities, possibilities and benefits (think of the warming sun).","is_correct":False,"justification":"1"},
            {id:2,"body":"Used as a master hat to control the thinking process.","is_correct":False,"justification":"2"},
            {id:3,"body":"Used to discover why some ideas will not work, this hat inspires logical negative arguments.","is_correct":False,"justification":"3"},
            {id:4,"body":"Used to think about facts, figures, and other objective information.","is_correct":False,"justification":"4"},
            {id:5,"body":"Used to elicit the feelings, emotions, and other non-rational but potentially valuable senses, such as hunches and intuition (think of a red heart).","is_correct":True,"justification":"5"},
            {id:6,"body":"Used to find creative new ideas (think of new shoots sprouting from seeds).","is_correct":False,"justification":"6"}
        ]
    },User.objects.get(id=3),4)

    new_quiz({
        "tag":"TST",
        "body":"Which of the following are internal qualities of a software product?",
        "opt_text":"",
        "options":[
            {id:1,"body":"Maintainability, robustness, portability, efficiency, correctness.","is_correct":False,"justification":"1"},
            {id:2,"body":"Robustness, reusability, portability, efficiency, correctness.","is_correct":False,"justification":"2"},
            {id:3,"body":"Maintainability, reusability, portability, efficiency, correctness.","is_correct":False,"justification":"3"},
            {id:4,"body":"Reliability, robustness, efficiency, maintainability, reusability","is_correct":False,"justification":"4"},
            {id:5,"body":"Correctness, reliability, robustness, efficiency, usability.","is_correct":False,"justification":"5"},
            {id:6,"body":"Maintainability, reusability, portability, interoperability.","is_correct":True,"justification":"6"}
        ]
    },User.objects.get(id=1),4)