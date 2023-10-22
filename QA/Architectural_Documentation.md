## Architectural Documentation for the Quirked Up Software Project


## Overview

    This document presents the architectural documentation for the "Quirked Up Software" project, a web-based quiz application developed as part of the "Software Engineering" course. The project consists of a database, a frontend, and a backend.

* Database: SQLite
* Frontend: CSS and JAVASCRIPT with React
* Backend: Python with Django


## Directory Structure

    The project uses an organized directory structure as follows:

        - ARCH: This folder contains documents related to the system's architecture, including technical specifications, architecture diagrams, and architectural decisions.

        - DEP: The DEP folder contains information related to the application's deployment, including deployment scripts, production server configurations, and deployment procedures.

        - DES: Here are documents related to the system's design, including user interface mockups, wireframes, and style guides.

        - DEV: The DEV folder is where source code and other development-related artifacts are stored.

        - ENV: This folder contains information about the development and production environment, including environment variables, environment configurations, and initialization scripts

        - PM: The PM folder is related to project management, including project planning documents and weekly time logs.

        - PROC: Documents related to project processes are stored here, including development guidelines, commit message recommendations, and more.

        - PROD: This folder contains information and scripts related to the production environment, such as production server configurations, production deployment scripts, and performance monitoring.

        - QA: The QA folder contains documents related to quality assurance, including test plans, test reports, and quality assurance procedures.

        - REQ: The REQ folder contains documents related to project requirements, including functional and non-functional requirements specifications.


## Communication between Components

    Communication between the system's components is accomplished through HTTP requests. The frontend makes requests to the backend to retrieve or send data, and the backend communicates with the database to retrieve or persist information. Communication between the parts of the system is essential for the proper functioning of the application.


## Architecture Diagram

    In the ARCH folder, there is a simplified architecture diagram that illustrates the interaction between the key components of the system. This diagram provides an overview of the relationships between the frontend, backend, database, and other parts of the system.


## Architectural Decisions

    The primary architectural decisions made in the project include:

        - The choice of React and Django technologies for the frontend and backend, respectively, due to their familiarity and support for building robust web applications.
        - The decision to follow an MVC architectural pattern in the frontend to separate concerns of presentation, business logic, and data access.
        - The use of an SQL database for data storage.


## Security

    Security measures implemented in the project include proper authentication and authorization to protect user data, as well as recommended security practices such as input validation and encryption of sensitive data.


## Data Management

    The database is used to store the system's data, and the project includes regular backup routines to protect against data loss. Data management is essential to ensure data integrity and availability.


## Conclusion

    This architectural documentation provides an overview of the architecture of the Quirked Up Software project, describing its components, directory structure, architectural decisions, and performance considerations. The focus on scalability and security ensures that the system is robust and capable of meeting user needs.