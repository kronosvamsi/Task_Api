# Task_Api
This is  a task manager api web application. It is a task manager where it manages the task by CRUD operations.In general tasks are records with Id,name,description stored in database.

### Set up details

1. Create a new folder with proper name
2. Open terminal and cd path to created folder path.
3. Create a new python env and activate it. 
4. Download the repo from url
5. Install the requirements and dependencies using code: ``` pip install requirements.txt ```
6. In terminal cd path to root folder(path where manage.py exists)
7. Run the coomand : ``` python manage.py runserver ``` (If Python 3 exists in env, no problem. Otherwise, use python3). Server gets started
8. Run the command :  ``` python manage.py makemigrations ```  and  ```python manage.py migrate ``` -- It is for creating tables in database

## Basic usage ##
Now go to new terminal (with server terminal  running)
Here we can use following commands to create , update , list, delete tasks.
1.```list ``` : To list the no of tasks present currently.
2. ```create  Id  name description ``` : To create the new task 
3. ``` update Id``` : To update the new task and make changes to existed record
4. ``` delete  Id``` : To delete the task which is not in use.


