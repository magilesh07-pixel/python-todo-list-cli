import json

print("=====To-do-List Application=====")

tasks = []

try:
    with open("tasks.json","r") as file:
        tasks = json.load(file)

except:
    tasks = []

def save_tasks():
    with open("tasks.json","w") as file:
        json.dump(tasks,file)

while(1):
    print("\n   Menu")
    print("\n1.Add task")
    print("2.View task")
    print("3.Delete task")
    print("4.Exit")

    choice = int(input("Enter your choice : "))

    if(choice==1):
        print("\nYou chose : Add task")
        task = input("Enter new task : ")
        tasks.append(task)
        print("\nTask added successfully")

    elif(choice==2):
        if(len(tasks)==0):
            print("\nNo tasks available")
        else:
            print("\nYou chose : View task\n")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])

    elif(choice==3):
        if(len(tasks)==0):
            print("\nNo tasks to delete")
        else:
            print("\nYour tasks")
            for i in range(len(tasks)):
                print(i+1,".",tasks[i])

            delete_index = int(input("\nEnter the number of the task to be deleted : "))-1
            if(delete_index>=0 and len(tasks)>delete_index):
                removed_task = tasks.pop(delete_index)
                print("\nRemoved list : ",removed_task)

            else:
                print("\nInvalid task number")

    elif(choice==4):
        print("\nExiting Program...!")
        break

    else:
        print("\nInvalid choice! Enter a valid choice(1/2/3).")

    
