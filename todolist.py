# Ken's Todo List Program
import os
import sys
from pathlib import Path

todo_path = Path.cwd()
print(todo_path)
#os.makedirs

#Start up Menu (W.I.P)
Menu_banner = r"""
------------------
1) View Saved Lists
2) Open List
3) Create List
3) Delete list
4) Exit
------------------
"""
print(Menu_banner)
main_menu_option = int(input("\nChoose a option: "))
if main_menu_option == 1:
    print("Option not available at the moment")
if main_menu_option == 2:
    print("Option not available at the moment")
if main_menu_option == 3:
    name_of_file = input("What would you like to name the file to save: ")
    try:
        with open(name_of_file, "r", encoding="utf-8") as f:
            todo_list = [line.strip() for line in f]
    except FileNotFoundError:
        todo_list = []
if main_menu_option == 4:
    file_to_del = input("Which file do you want to delete?")
    try:
        if os.path.exists(file_to_del):
            os.remove(file_to_del)
    except FileNotFoundError:
        print(f"File: {file_to_del} does not exist")
    



def savelist():
    with open(name_of_file, "w", encoding="utf-8") as f:
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
        
#Set piority of the tasks
def set_piority():
    # TODO: requires more intermediate concpets to implement feature
    print("Priority configuration not yet implemented.")
    
    
#enumartate def
def enumarate_tasks():
    for index, item in enumerate(todo_list):
        print("Task" + str(index) + ' is: ' + item)

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
        userinput = input("Add, delete, show, configure, or quit? ").lower()

        if userinput in ("add", "a", "+"):
            insertTask()
        elif userinput in ("delete", "d", "-"):
            deleteTask()
        elif userinput in ("show", "s"):
            showlist()
        elif userinput in ("configure", "c", "edit"):
            set_piority()
        elif userinput in ("enum"):
            enumarate_tasks()
        elif userinput in ("quit", "q", "exit", "stop"):
            print("Goodbye!")
            break
        else:
            print("Invalid input, please try again.")


def todolist():
    print("This is your todo list program")
    listprompt()


todolist()#start program
# End of Ken's Todo List Program
