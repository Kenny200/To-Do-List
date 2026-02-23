# Ken's Todo List Program

try:
    with open("mylist.txt", "r", encoding="utf-8") as f:
        todo_list = [line.strip() for line in f]
except FileNotFoundError:
    todo_list = []


def savelist():
    with open("mylist.txt", "w", encoding="utf-8") as f:
        for task in todo_list:
            f.write(task + "\n")


def insertTask():
    while True:
        task = input("Insert task (or type quit/back): ").strip()

        if task.lower() in ("back", "b"):
            return
        if task.lower() in ("quit", "q", "exit", "stop"):
            break

        if not task:
            print("Task cannot be empty.")
        elif task in todo_list:
            print("Task already exists.")
        else:
            todo_list.append(task)
            savelist()
            print(f"Task '{task}' has been added.")

#Delete tasks from todo list
def deleteTask():
    if not todo_list:
        print("No tasks to delete.")
        return

    while True:
        showlist()
        taskdel = input("Task to remove (or type quit/back): ").strip()

        if taskdel.lower() in ("quit", "q", "exit", "stop"):
            break
        if taskdel.lower() in ("back", "b"):
            return

        if taskdel not in todo_list:
            print("Task not found.")
        else:
            todo_list.remove(taskdel)
            savelist()
            print(f"Task '{taskdel}' has been removed.")
            return

#Show todo list
def showlist():
    if not todo_list:
        print("Your todo list is empty.")
    else:
        print("Your todo list:")
        count = 1
        for task in todo_list:
            print(f'{count}. {task}')
            count += 1
        userinput = input("Go back to main menu? (y/n): ").lower()
        if userinput in ("y", "yes"):
            listprompt()
        

#Main menu
def listprompt():
    while True:
        userinput = input("Add, delete, show, or quit? ").lower()

        if userinput in ("add", "a", "+"):
            insertTask()
        elif userinput in ("delete", "d", "-"):
            deleteTask()
        elif userinput in ("show", "s"):
            showlist()
        elif userinput in ("quit", "q", "exit", "stop"):
            #print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")


def todolist():
    print("This is your todo list program")
    listprompt()


todolist()#start program
# End of Ken's Todo List Program