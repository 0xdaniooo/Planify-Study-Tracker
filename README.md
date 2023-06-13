# Planify-Study-Tracker
A website built with Django REST Framework + Bootstrap 5 aimed at students wanting to track their studies effectively in an intuitive manner. 

See it in action here: https://www.youtube.com/watch?v=s_OYAgo6N7g


## About
This idea has originally been cultivated and developed by me and my teammates for our team project module in our first year of university (more info on the inspiration and backstory can be found on the website's landing page). Unfortunately, with our limited programming experience and lack of time, we never managed to bring it to the level we had aspired to. Wanting to push my skills further, I decided to develop this idea from the ground up using what I had learnt and made our vision become a reality at last.


## Features
- Track completion of tasks across multiple weeks
- Mark whether you've achieved completion or not (or blank it out)
- Keep track of however many tables, tasks or weeks you wish
- Likelihood of passing calculated for each table
- Account creation and management (login, signup, username and password changes, deletion)


## Usage
Make sure to install Python3 first before proceeding

- Install Django + other dependancies (run each command seperately)
```
python -m pip install Django
pip install djangorestframework
pip install django-crispy-forms
pip install crispy-bootstrap5
```

- Download the planify project files and navigate to the directory where the manage.py file is present

- Start the server by running the manage.py file with python3
```
python manage.py runserver
```

- Head to http://127.0.0.1:8000/ where the server will be running
- You can stop running the server anytime as any changes will be saved onto the database (no data will be lost)


## Landing Page
![What is Planify](/Imgs/WhatIsPlanify.png)

![Planifys Backstory](/Imgs/PlanifysBackstory.png)

![Then vs Now](/Imgs/ThenVsNow.png)


## Main Functionality
![Get Started](/Imgs/GetStarted.png)

![Planify](/Imgs/Planify.png)

![Week Interactions](/Imgs/WeekInteractions.png)

![Delete Task](/Imgs/DeleteTask.png)


## Account Management
![Login](/Imgs/Login.png)

![Sign Up](/Imgs/SignUp.png)

![Edit Account](/Imgs/EditAccount.png)

![Change Password](/Imgs/ChangePassword.png)

![Delete Account](/Imgs/DeleteAccount.png)
