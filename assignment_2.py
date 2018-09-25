# You are responsible for creating a TODO list app. 
# Here are the requested features for the TODO list app:
#  
# - User should be able to add task by adding the title of 
# the task 
#
# - User should be able to enter priority of the task 
#
# - User should be able to view all the tasks 
#
# - User should be able to remove the tasks 
#
# - User should be able to quit the app when "q" is pressed 

#HARD MODE: 

#- User should be able to sort the tasks based on priority 
class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

def promptUserForInput():
    while True:
        try:
            input_task = input('What is the task name? ') 
            input_priority = int(input('What is the task priority (Scale of 1-10 with 1 being most important)? '))
        except ValueError:
            print("********* Please enter a priotity number between 1 and 10. **********")
            input_priority = int(input('What is the task priority (Scale of 1-10 with 1 being most important)? '))
        
        return (input_task, input_priority)

(input_task,input_priority) = promptUserForInput()
task = Task(input_task, input_priority)
tasks = []
task_join = str(task.priority) + "-" + task.title
tasks.append(task_join)
 
def choice_input():
            choice = input('Press 1 to add another task\nPress 2 to view tasks\nPress 3 to remove task\nPress 4 to sort tasks\nPress Q to Quit\n\n')
            return choice

def sort():
    tasks.sort()

while True:
    try:
        choice = choice_input()

        if (choice == "Q" or choice == "q"):
            break
        elif (choice == "1"):
            (input_task,input_priority) = promptUserForInput()
            task = Task(input_task, input_priority)
            task_join = str(task.priority) + "-" + task.title
            tasks.append(task_join)
        elif (choice == '2'):
            print(f'{tasks}\n\n')
            choice = choice_input()
        elif (choice == '3'):
            break
        elif (choice == '4'):
            sort()
            print(f'{tasks}\n\n')
            choice = choice_input()

        
    except ValueError:
        print("Try again")


print(tasks)
tasks.sort()
print (tasks)

