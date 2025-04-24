from django.shortcuts import render
from django.http import JsonResponse
from .models import Tasks
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def list_tasks(request):
    
    data =list(Tasks.objects.values())
    print("list items --")
    if  len(data) <=0:
        return JsonResponse({"note":"there are no tasks currently !"},safe=False)
    
    else:

     return JsonResponse(data,safe=False)

@csrf_exempt
def create_task(request):
   
   data = json.loads(request.body)
   item = Tasks.objects.create(id=data['id'],name=data['name'], description=data['description'])
   return JsonResponse({'id': item.id, 'name': item.name, 'description': item.description}, status=201)
   
   
def update_tasks(request,item_id):
   data=json.loads(request.body)
   task_item=Tasks.objects.get(id=item_id)
   task_item.name=data['name']
   task_item.description=data['description']
   task_item.save()
   return JsonResponse({'id':task_item.id,'name':task_item.name})

@csrf_exempt
def delete_task(request, item_id):
        item = Tasks.objects.get(id=item_id)

        item.delete()
        return JsonResponse({'message': 'Item deleted successfully'}, status=204)
   
      
