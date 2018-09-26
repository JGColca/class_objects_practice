# You are responsible for creating an app that manages groceries. 
# Your groceries are characterized by Shopping Lists which can contain grocery items. 
# Here are the features you need to implement: 
# * You need to ask the user for the input. 

# - A user should be able to create a shopping list. A shopping list consists of a title and description. 
# Example = Fiesta, Walmart, Sams Club, Cosco, Randalls etc 

# - A user should be able to add multiple shoppings lists 

# - Give user an option to display the list 

# - A user should be able to add a grocery items to a particular shopping list. A grocery item consists of a title. 
# Example Milk, Cookies, Paper, Napkins, Soda, Chips etc 

# Fiesta
# Milk, Soda, Fish 

# Walmart
# Paper, Napkins, Plate, Chips 

# Sams Club 
# Chicken, Beef, Eggs, Sugar, Salt, Pepper, Honey

# Class named Shopping List Class with title and description needed to call class
class Shopping_List_Class:
    def __init__(self, title, description):
        self.title = title
        self.description = description

#Function for asking user to create shopping list
def prompt_user_to_create_shopping_list():
   
    input_list_name = input('What is the list name? Enter q to stop   ')
    if input_list_name.lower() == "q":
        input_list_description = ""
    else:
        input_list_description = input('Enter a list description:  ')
    return input_list_name, input_list_description
    
# Array to hold shopping list objects created by user by calling shopping list class
shopping_lists_array = []

# Loop to continually ask user to create shopping lists unless user ends loop by pressing "q"
while True:
    (input_list_name, input_list_description) = prompt_user_to_create_shopping_list()           
    if (input_list_name.lower() != "q"):
        shopping_list = Shopping_List_Class(input_list_name, input_list_description)
        shopping_lists_array.append(shopping_list)
    elif (input_list_name.lower() == "q"): 
        break
    
# Loop to print each individual list in the shopping_lists_aaray
for list in shopping_lists_array:
    print (f'{list.title} - {list.description}')

#Function for asking user to create a grocery item
def prompt_user_to_create_grocery():
    input_grocery = input('What is the grocery name? Enter q to stop   ')
    return input_grocery

#  class named Grocery Class with item_name needed to call class
class Grocery_Class:
    def __init__(self, item_name):
        self.item_name = item_name

# Array to hold grocery objects created by user by calling grocery class
groceries_array = []

# Loop to continually ask user to create grocery items unless user ends loop by pressing "q"
while True:
    try:
        (input_grocery) = prompt_user_to_create_grocery()
        if (input_grocery.lower() != "q"):
            grocery = Grocery_Class(input_grocery)
            groceries_array.append(grocery)
        else:
            break
    except ValueError:
        print("Please enter letters only")

# Loop to print each individual grocery item in the groceries_array
for list in groceries_array:
    print (list.item_name)

# List manager class with no parameters to call class
class List_Manager_Class:
    def __init__(self):
        self.prompt_user()

# Function to ask user to select from main menu
    def prompt_user(self):
        user_selection = input("Menu\n 1. Press 1 to create list\n 2. Press 2 to add groceries\n 3. Press Q to Quit")
        


#Create object list manager by calling List_Manager_Class
list_manager = List_Manager_Class()

#Calling prompt_user function using list_manager object
list_manager.prompt_user()