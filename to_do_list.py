task=[]
def add_task():
    choice=input(f"add your task: ")
    task.append(choice)
    print(f"task added successfully")
def view_task():
    i=1
    for x in task:
        print(f"task {i}: {x}")
        i+=1
def completed():
    task_num=int(input(f"enter ur task num that u competed: "))
    if 0<=(task_num -1) <len(task):
        task[task_num -1]=f" {task[task_num -1]} is completed"
        print(f"marked as completed")
        
    else:
        print(f"the task does not exist")
def remove():
    task_num=int(input(f"enter the task u want to delete: "))
    if 0<=(task_num - 1)< len(task):
        task.remove(task[task_num -1 ])
        print(f"deleted successfully")
    else:
        print(f"the task does not exist")
            
def welcome():
    print(f"welcome to our to do list ")
    print(f"1. add task")
    print(f"2. view task")
    print(f"3. completed task")
    print(f"4. deleted task")
    print(f"5. exit")
def main():
    welcome()
    while True:
        choice=input(f"enter ur number: ")
        if choice =="1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice=="3":
            completed()
        elif choice=="4":
            remove()
        elif choice=="5":
            print(f"thank u for using this")
            return
        else:
            print (f"invalid num")
main()
