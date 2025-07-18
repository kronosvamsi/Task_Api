# Task_Api
This is  a task manager cli tool application. By the help of cli tool, we can create ,update, delete the task by using terminal based commands.With the help of cli tool we can directly perform  CRUD operations in terminal. In general tasks are records with Id,name,description stored in database.

### Set up details

1. Create a new folder with proper name
2. In terminal , ```cd folder-path ```
3. Download the repo from url [link](https://github.com/kronosvamsi/Task_Api.git)
4. `cd repo folder`,create a new python env and activate it.
5. Install the requirements and dependencies using cmd: ``` pip install -r requirements.txt ```
6. Now, ``cd path `` to main folder(path where manage.py exists)
7. Run the coomand : ``` python manage.py runserver ``` (If Python 3 installed in env, no problem. Otherwise, use python3). Server gets started
8. Run the command :  ``` python manage.py makemigrations ```  and  ```python manage.py migrate ``` --  For creating tables in database


## Basic usage 

Here we can use following commands to create , update , list, delete tasks.
1. ``` list ``` : To list the tasks present in database if exists,  otherwise empty list show up -> ```[]```
2. ``` create id name description ``` : To create the new task
3. ```update id ``` : To update the existed task otherwise  ``` Task doesnt exists ``` error
4.  ``` delete id ``` : To delete the task

## Examples 
Now go to new terminal (with server terminal  running)

!["server running"](https://github.com/kronosvamsi/Task_Api/blob/main/static/Screenshot%20from%202025-04-25%2012-50-03.png)

Above shows the image of server terminal. Beside that another terminal opened

Run following commands in other terminal to test the api :
1. ``` python cli_tool.py list ``` : This command will list all the tasks present in database .

2.  ![ List image](https://github.com/kronosvamsi/Task_Api/blob/main/static/Screenshot%20from%202025-04-25%2012-50-15.png)

3.  ``` python cli_tool.py create id(int) name(str) description(str) ``` : This command will create the new task  and add it to database

4.  ![Add new task](https://github.com/kronosvamsi/Task_Api/blob/main/static/Screenshot%20from%202025-04-25%2013-17-42.png)

5.  ```python cli_tool.py delete id``` : This command will delete the exist task

6.  ![Delete task](https://github.com/kronosvamsi/Task_Api/blob/main/static/Screenshot%20from%202025-04-25%2013-19-22.png)


Finally you have the task manager api with cli tool to perform crud operations.You can also see the responses from server

![server response](https://github.com/kronosvamsi/Task_Api/blob/main/static/Screenshot%20from%202025-04-25%2013-20-37.png)

>[!NOTE]
>An update regarding command response. Now you will get response after succesful exection of command.
   
   







 


