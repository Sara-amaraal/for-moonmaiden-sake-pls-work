# How to run the project on a local machine?

- Follow all the steps in the order they appear in this file.

- Text that is is formatted like `this` is a command that you should be entered in a terminal.

- Open three terminals. All the commands to initialize the project will be entered in these three terminals. One terminal will be used for the frontend, another for the backend, and another to add test data to the database.

## Frontend

### NodeJS latest version must be installed

You can download it [here](https://nodejs.org/en/download/).

Then, follow these steps in the frontend terminal:

- `cd DEV/frontend`  - Starting from the repository root

- `npm install` -  Installs all the frontend dependencies (only needs to be used the first time, else skip this step)

- `npm start` - Launches the React app

## Backend

### Python 3.10 or higher version must be installed

You can download it [here](https://www.python.org/downloads).

If you already have python installed, you can check the version by running `python --version`

Then, follow these steps, in the backend terminal:

- `cd DEV/backend` - Starting from the repository root

- (Optional) Create/activate your virtual environment for the project, if you don't know how to do this ignore this step

- `pip install -r requirements.txt` - Installs all the backend dependencies (only needs to be used the first time, else skip this step)

- `python manage.py migrate` - _Updates_ the needed backend contents (only needs to be used the first time, else skip this step)

- `python manage.py runserver` - Launches the Django database

## Add test data to the database

### Backend needs to be successfully running already

Then, follow these steps, in the database test data terminal:

- `cd DEV/backend` - Starting from the repository root

- `python manage.py runscript init_db`

This is will register the following 3 accounts in the database, with test data already associated with them:

- Username: justAUser1 | password: admin123
- Username: justAUser2 | password: admin123
- Username: justAUser3 | password: admin123

**You only needed to do this step once unless you reset the
database, by deleting the sqlite file. Otherwise the test data will stay there.**

Either way, if you do run it again when you shouldn't, it will not cause any problems, and only displays a unique constraint error.
