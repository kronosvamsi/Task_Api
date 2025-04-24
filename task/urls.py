from django.urls import path

from  .views import *

urlpatterns=[

    path("items/",list_tasks,name="list_task"),
    path("create/",create_task,name="create_task"),
    path("update/<int:item_id>",update_tasks,name="update_task"),
    path("delete/<int:item_id>",delete_task,name="delete_task")
]