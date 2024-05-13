
# Using This Template 

This template was designed by [Reagan Barrington](https://github.com/ReBarrington) in an effort to help analysts kickstart a HYC full-stack web application using React and Python. It is structured into two main directories: `frontend` and `backend`, designed to offer a simple and organized development environment. The template is ideal for kickstarting POC projects and reducing initial setup time.

Looking for a different template?
- [Python Command Line Interface Template](https://github.com/Kingsmen-Software/PythonCLITemplate)

## Requirements

This template requires Node.js and Python to be installed on your machine. Ensure you have the latest versions to avoid compatibility issues.

Steps to use this template:
1. Click the green "Use this template" button at the top of the repository.
2. Name your repository and give it a description.
3. Clone your new repository to your local machine. [Video Tutorial Here](https://www.youtube.com/watch?v=ILJ4dfOL7zs)
4. Follow the instructions in the ['Getting Started' section](#getting-started) of the README to set up your project.

I hope you find this helpful! Please remember to update the README with your project information and remove this section before pushing your project to GitHub. Thank you!

-------------------------------------------------------------------------------------------------------------

# [Project Name Here]

## Overview

Give an overview of the project and its goals here.

<br>

## Directory Structure

| Folder    | Description                                         |
|-----------|-----------------------------------------------------|
| `frontend`| Contains all React code and related configurations. |
| `backend` | Houses the Python backend code.                    |

<br>

## Getting Started

### Setting Up the Frontend
Navigate to the `frontend` directory:
```
cd frontend
```

Install the necessary dependencies:
```
npm install
```

Run the frontend:
```
npm start
```

### Setting Up the Backend
Navigate to the `backend` directory:
```
cd backend
```

First you will need to create a virtual environment for your project. It is recommended you name the virtual environment venv since that is the default and already part of .gitignore. To do this, open up a new terminal and navigate to the project directory and run the following command:
```
python -m venv venv
```

This will create a virtual environment inside of your project so that your installed dependencies will be scoped to this project only. Next you will need to activate your virtual environment that was just created by running the following command:
```
.\venv\Scripts\activate

Note: If you use Mac the command should be:
source ./venv/bin/activate
```
or this command if you named your virtual environment something different
```
.\<virtualEnvironmentName>\Scripts\activate

Note: For mac use:
source ./{virtualEnvironmentName}/bin/activate
```
You will notice when you have changed to your virtual environment because your terminal will display the name of your environment. Next you will need to install the necessary project dependencies by running the following command:
```
pip install -r requirements.txt
```
This will install the necessary project dependencies. Next you will need to create a .env file in your root app folder if it does not already exist. There is a .env.example file with env variables you need to specify in .env file. Then you will need to populate the various values.

### Run the backend:
Uvicorn comes with the fastapi install and is a web server for python that project runs in.

Using visual studio code for debugging:

Select Run and then click Start Debugging. An alternative is to use the hotkey F5.

Using the terminal for no debugging:
```
uvicorn app.main:app --port 8000
```
Note: Flag --reload can be added for server to automatically reload on code changes:
```
uvicorn app.main:app --port 8000 --reload
```
If that does not start successfully you may need to change your port number over to 8001.
