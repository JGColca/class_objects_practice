
# Friend Class
class Friend:
    def __init__(self, friend_name):
        self.friend_name = name
#Person Class
class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.unique_friends = []
        self.unique_greeting_count = 0

#Function for Greeting Someone for Object Person
    def greet(self, other_person):
        self.greeting_count += 1
        print ('Hello %s, I am %s!' % (other_person.name, self.name))
        if other_person.name not in self.unique_friends:
            self.unique_friends.append(other_person.name)
            self.unique_greeting_count += 1

#Function for Printing Contact Information for Object Person    
    def print_contact_info(self):
        print (f'{self.name}\'s email: {self.email}, {self.name}\'s phone number: {self.phone}')

#Function for Printing Friends of Object Person
    def print_friends(self):
        print (f'This is a list of {self.name}\'s friends : {self.friends}')

 #Function for adding Friends of Object Person   
    def add_friend(self, friend_name):
        self.friends.append(friend_name)

 #Function for Number of Friends of Object Person   
    def num_friends(self):
        print (f'This is how many friends {self.name} has: {len(self.friends)}')
    
#Function for Printing Greeting Count of Object Person
    def print_greeting_count(self):
        print (f'This is how many people {self.name} has greeted: {self.greeting_count}')
        
#Function for Printing Number of Unique People Greeted of Object Person    
    def num_unique_people_greeted(self):
        print (f'This is how many unique people {self.name} has greeted: {self.unique_greeting_count}')

#Function for List of Unique Greets of Object Person    
    def print_unique_greeting_list(self):
        print (f'This is a list of {self.name}\'s unique people greeted : {self.unique_friends}')

#Function for Object information when Class is called  
    def __repr__(self):
        return (f'This is a return of atrributes when a class is called: {self.name}, {self.email}, {self.phone}')
        
#People
sonny = Person("Sonny", "sonny@hotmail.com", "438-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
deeann = Person("DeeAnn", "deann@gmail.com", "555-555-5555")

#Greets
sonny.greet(jordan)
jordan.greet(sonny)
sonny.greet(jordan)

#Call function for Printing Contact Info
sonny.print_contact_info()

#Print person Information using .attribute
print (sonny.name, sonny.email, sonny.phone)
print (jordan.name, jordan.email, sonny.phone)

#Declaring a Person as a friend
friend1 = sonny
friend2 = jordan

#Adding a friend using add friend function
jordan.add_friend(friend1.name)
sonny.add_friend(friend2.name)

#Printing friends and number of friends using print friends and number of friends functions
sonny.print_friends()
sonny.num_friends()

#Printing friends and number of friends using print friends and number of friends functions
jordan.print_friends()
jordan.num_friends()

#Counting Unique People Greeted using unique people greeted function
sonny.num_unique_people_greeted()

#Greeting someone and counting unique people greeted using unique people greeted function
sonny.num_unique_people_greeted()

#Greeting someone and counting unique people greeted using unique people greeted function
sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()

#Greeting someone and counting unique people greeted using unique people greeted function
sonny.greet(jordan)
sonny.num_unique_people_greeted()

#Greeting someone and counting unique people greeted using unique people greeted function
sonny.greet(deeann)
sonny.num_unique_people_greeted()

#Print total people greeted
sonny.print_greeting_count()

#Print number of unique people greeted
sonny.num_unique_people_greeted()

#Print list of names of unique people greeted
sonny.print_unique_greeting_list()


#Vehicle Class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
#define function for printing vehicle information
    def print_info(self):
        print (f'This is printed using print_info function: {self.year}, {self.make}, {self.model}')

#Provide car attributes of vehicle class
car = Vehicle("Toyota", "Camry", "2016")

#Print attribute information using "." notation
print (f'This is printed using \".\" notation for each attribute outside of a function: {car.make}, {car.model}, {car.year}')

#Print car attributes using function for printing vehicle informations
car.print_info()

