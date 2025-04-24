
from django.core.management.base import BaseCommand, CommandError
from ...models import Tasks



class Command(BaseCommand):
    help="This is task scheduler command"

    def add_arguments(self, parser):
        
        parser.add_argument('-l',"-list",action="store_true")
        parser.add_argument('--add_task', nargs='+',help="list items")
        parser.add_argument('--del_task',nargs='+', help="del item")
    
    def handle(self,*args,**options):
        
        if options['l']:
            task_list=list(Tasks.objects.all())
            task_names=[{task.id:task.name} for task in task_list]
            # arr=[]
            # for val in task_list:
            #     arr.append(val)

            self.stdout.write(f"The tasks added  are :{task_names}")
        if options['add_task']:
            id=input("Enter the Id :")
            name=input("Enter the task name :")
            desc=input("Enter the description :")
            task=Tasks(id=int(id),name=name,description=desc)
            task.save()
            self.stdout.write(f"the task created :{task.name}")
        
        if options['del_task']:
            try:
                # print(options['del_task'])
                id,=options['del_task']
                task=Tasks.objects.get(id=int(id))
                self.stdout.write(f"The task gets deleted : {task.name}")
                task.delete()
            except Tasks.DoesNotExist:
                raise CommandError("The task with id %s was not found "%id)
            
        
        
