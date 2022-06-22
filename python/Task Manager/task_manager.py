#=====importing libraries===========
'''This is the section where you will import libraries'''

# 30/04/2022
# Scott-Reece Morgan
# FCS L1T19: Capstone project II

# A python program that requires a user to log in to access information
# regarding assigned tasks.
#
# The program is designed to accomodate two types of users: admin users are
# are allowed to add personnell to the system and view statistics of tasks;
# where normal users arent offered these options.
#
# All user input apart form the menu selection is appended to the appropriate
# .txt file
#
# RESOURCES:
# > How to open two files at once
#       https://www.geeksforgeeks.org/how-to-open-two-files-together-in-python/
# > How to add data to the bottom of the file
#       https://stackoverflow.com/questions/13248020/whats-the-difference-between-r-and-a-when-open-file-in-python


#                                   FUNCTIONS

def list_content(filename):
     """A function that opens a .txt file and stores its content in a list"""
     contents = []
     with open(filename, 'r+', encoding = 'utf-8') as file:
        for line in file:
           contents.append(line.replace("\n", "").split(", "))

     return contents


     
def reg_user():
     """A function that registers a new user.
        a while loop is used to continuously prompt admin to enter a user name
        that doesnt already exist. this is done using an if-else flow control
        to check if the entered user name already exists in a list of usernames.

        a similar method is used to confirm the new password entered. the new
        username and password is then appended to the appropriate .txt file"""

     # New username
     match = False
     while (True):
         new_username = input("New user username :\t").strip()
         if (new_username in usernames):
             print("User already exists, please enter a new username.")
         else:
             break

     # New password
     new_password = input("New user password :\t").strip()
     while (not match):
         confirm_pass = input("Confirm password :\t").strip()
         if (confirm_pass == new_password):
             match = True
         else:
             print("\nPassword not confirmed, please confirm password.\n")


     # Storing new user information to .txt file
     with open('user.txt', 'a+') as user:
         user.write(f"\n{new_username}, {new_password}")

     return

def add_task():
     
     """A function that assigns tasks to a specific user.
        This is done by appending information pertaining to the task
        and the user to the appropriate .txt file
     """
     # User input
     task_user = input("Please enter the username of the person whom the \
task is assigned to :\t").strip()
     task = input("Please enter the title of the task :\t").strip()
     task_desc = input("Please enter a description of the task :\t").strip()
     task_due = input("Please enter the due date of this task (DD/MM/YYYY) :\t").strip().replace("(", "").replace(")", "")
     date = input("Please enter todays date (DD/MM/YYYY) :\t").strip().replace("(", "").replace(")", "")

     # Appending user input to tasks.txt
     with open('tasks.txt', 'a+') as tasks:
         tasks.write(f"\n{task_user}, {task}, {task_desc}, {date}, \
{task_due}, No")


def view_all():
     """A function that reads, processes and outputs information from a .txt
        file.
        Each line in the file is read, processed (stripped of unwanted
        information and split into a list) and then output in a way that is easy
        read and understand.
        """
     
     with open('tasks.txt', 'r+', encoding = 'utf-8') as tasks:
         for line in tasks:
             task_info = line.replace("\n", "").split(", ")
             # Sub if-elif flow control to check task completion
             if ("No" in task_info):
                 status = "Incomplete"
                 
             elif ("Yes" in task_info):
                 status = "Complete"
                        
             # Displaying task info to user     
             print(f'''\n
Task:               {task_info[1]}
Assigned to:        {task_info[0]}
Date assigned:      {task_info[3]}
Due date:           {task_info[4]}
Task status:        {status}
Task description:
\t{task_info[2]}''')


def view_mine():
    """ A function printing out the tasks assigned to a specific user.

         A for loop is used to iterate through all the tasks stored in a list,
         an if-elif flow control is used to test the opening characters of each
         line in relation to the user name. if passed the info is assigned a
         task number and the information is printed in a readable manner

         the user is then optioned with editting a task (marking as complete ,
         changing the due date or reassigning the task to a new user) this is
         done by using nested if else flow control and various conditions """

     
    task_num = 0
    
    print("\nThese are your tasks :")

    contents = list_content('tasks.txt')

    # Checking for the users tasks and assigning each task anumber
    for task_info in contents:
        if (username in task_info):
            task_num += 1

            # Checking Task status
            if ("No" in task_info):
                status = "Incomplete"
            elif ("Yes" in task_info):
                status = "Complete"

            # Displaying task info to user   
            print(f'''\n
{task_num}.
Task:               {task_info[1]}
Date assigned:      {task_info[3]}
Due date:           {task_info[4]}
Task status:        {status}
Task description:
\t{task_info[2]}''')
            
    # User prompt to edit tasks or return to the main menu 
    while(True):
        action = int(input("""\n
To edit a task, enter the task number;
To return enter -1.\n
:\t""").strip().replace(".", ""))

        # checking if a valid option was entered
        if (-1 > action > task_num ):
            print("You have entered an invalid option.\n")

        else:
            break
            
    # returning to the main menu
    if (action == -1):
        return

    else:
        # Code used to edit the displayed tasks
        
        task_count = 0

        # User prompting
        action2 = input('''
\nSelect one of the options below:
c - mark as complete
e - edit the task

:\t''').lower().strip()

        # Flow control to sort user choice.
        if (action2 == "c"):

            # the tasks content is filtered through for tasks assigned to the
            # user, increases the count when a task is found , and when the count
            # matches the task number entered , the task is marked as complete
            for task_details in contents:
                if (username in task_details):
                    task_count += 1
                    if (task_count == action):
                        task_details[task_details.index("No")] = "Yes"
                        print("Task marked as complete.")

                    
        elif (action2 == "e"):

            # the tasks content is filtered through for tasks assigned to the
            # user, increases the count when a task is found , and when the count
            # matches the task number entered , the user is prompted with a new
            # set of options.
            for task_details in contents:
                if (username in task_details):
                    task_count += 1
                    if (task_count == action):
                         
                        # If the task is not completed.
                        if ("No" in task_details):
                            action3 = input('''
Select one of the options below:
c - change due date
r - reassign to different user

:\t''').lower().strip()
                            # User input requested for each menu option for tasks
                            # that have not been completed
                            if (action3 == "c"):
                                task_details[3] = input("Enter new deadline:\t").strip()

                            elif (action3 == "r"):
                                task_details[0] = input("Enter User:\t").strip()
                                
                        # if the task has been completed                    
                        else:
                            print("This task is complete and cant be edited.")
                            return

        # Writing to task file with newly editted information
        with open('tasks.txt', 'w', encoding = 'utf-8') as tasks:
            for task_details in contents:
                tasks.write(", ".join(task_details) + "\n")

        return    
                
def gen_reports():
     """A function to generate reports on the tasks assigned and the status
        of tasks assigned to each user"""

     # User input
     date = input("Please enter todays date (DD/MM/YYY) :\t").strip()

     # Input processing and list generation
     date_numeric = int(date[::-1].replace("/", ""))
     tasks = list_content('tasks.txt')

     # Generation of task statistics using flow control and counts
     tot_tasks = len(tasks)
     yes_tasks = 0
     no_tasks = 0
     late_no = 0
     for task in tasks:
          task_due = task[4].replace("/", "")

          # Checks completeion status of tasks
          if ("Yes" in task):
               yes_tasks += 1

          elif ("No" in task):
               no_tasks += 1

               # checks if task is overdue by subtracting the due date from
               # the current date
               if ((int(task_due[::-1]) - date_numeric) < 0):
                    late_no += 1


     # Generation of user statistics
     users = list_content('user.txt')
     tot_user = len(users)
     overview = []
     # The statistics are generated for each user before moving onto the
     # next user
     for user in users:
          user_tasks = 0
          completed = 0
          incompleted = 0
          late = 0
          for task in tasks:
               task_due = task[4].replace("/", "") 
               if (user[0] in task):
                    user_tasks += 1
                    
                    # CHecks copleteion status of each task assigned to user                    
                    if ("Yes" in task):
                         completed += 1
                    elif ("No" in task):
                         incompleted += 1

                         # checks if task is overdue by subtracting the due date
                         # from the current date 
                         if ((int(task_due[::-1]) - date_numeric) < 0):
                              late += 1

          # Appending task to a list for .txt file writing
          overview.append(f"{user[0]}, {user_tasks}, {completed}, {incompleted}, {late}")

     
     # Writting of statistical information to two files
     # user_overview concerning the statistics of tasks assigned to each user
     # task_overview concerning the statistics of alla assigned tasks
     with open('task_overview.txt', 'w', encoding = 'utf-8') as tasko, open('user_overview.txt', 'w', encoding = 'utf-8') as usero:
          tasko.write(f"""As of {date}
Tasks recorded             : {tot_tasks}
Tasks completed            : {yes_tasks}
Tasks incomplete           : {no_tasks}
Tasks incomplete & overdue : {late_no}
Percentage incomplete  (%) : {(no_tasks/tot_tasks)*100}
Percentage overdue     (%) : {(late_no/tot_tasks)*100}""")

          usero.write(f"""As of {date}
Registered users : {tot_user}
Total tasks      : {tot_tasks}\n""")         
          for line in overview:
               temp = line.split(", ")
               usero.write(f"""\n{temp[0]}
Number of tasks  : {temp[1]}
% Of total tasks : {(int(temp[1])/tot_tasks)*100}
% Completed      : {(int(temp[2])/int(temp[1]))*100}
% Incompleted    : {(int(temp[3])/int(temp[1]))*100}
% Overdue        : {(int(temp[4])/int(temp[1]))*100}\n""")
               del temp

     return



#                                     SCRIPT

# LOGIN SECTION
# Usernames and passwords are read in from a .txt file, each line of the file is
# split into a temporary list then sorted into separate usernames and passwords
# lists with preserved indexing relating the username to the correct password.
#
# A while loop with nested if-else flow controls compares the entered username
# and password to the items in the list, first the username is checked and if
# passed the index of the item is retrieved and used to check the password.
# once the users credentials are verified , the while oop is exited.


# Variable and list declaration
usernames = []
passwords = []
credentials = False

# Reading in users login details.
with open('user.txt', 'r+', encoding = 'utf-8') as user:
    for line in user:
        temp = line.strip().split(", ")
        usernames.append(temp[0])
        passwords.append(temp[1])
        del temp

# User login procedure
while (not credentials):
    username = input("\nUSERNAME :\t")
    
    if (username in usernames):
        index = usernames.index(username)
        password = input("PASSWORD :\t")
        
        if (password == passwords[index]):
            credentials = True
            
        else:
            print("You have entered an incorrect username or password")
            
    else:
        print("You have entered an incorrect username")

# Administrator and normal user flow control
#
# A while loop nested withing an a if-else flow control (separating personell
# from administration), the while loop prompts the user with a menu of various
# options each option satisfies a condition in an if-elif-else flow control.
# if the condition is passed, it calls an appropriate function.
if(username == "admin"):
    while (True):
        #presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        menu = input('''\n
Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - generate reports
s - Statistics
e - Exit

: ''').lower()
        
        # Registration of new users, with while conditional to continually
        # prompt user input until escaped condition is satisfied.
        if (menu == 'r'):
            reg_user()
              
        # Addition of new tasks (stored to the appropriate .txt file)
        elif (menu == 'a'):
            add_task()


        # Viewing of all tasks regardless of user specificity
        elif (menu == 'va'):
            view_all()


        # Viewing of user specific tasks from all the tasks stored in the .txt
        # file.
        elif (menu == 'vm'):
            view_mine()

        # Database statistics regarding users and tasks
        elif (menu == 's'):
             gen_reports()

             # reading of generated reports
             with open('user_overview.txt', 'r+', encoding = 'utf-8') as usero, open('task_overview.txt', 'r+', encoding = 'utf-8') as tasko:
                  task_content = tasko.read()
                  user_content = usero.read()

             # processing and printing of editted information
             print(user_content[:59], task_content[48:] + '\n', user_content[60:], sep = "\n")

        # option to end the program    
        elif (menu == 'e'):
            print('Goodbye!!!')
            exit()

        # this option generates two types of reports in two .txt files labeled
        # user_overview.txt and task_overview.txt
        elif (menu == 'gr'):
            gen_reports()

        else:
            print("You have made a wrong choice, Please Try again")

# The start of the normal user menu options
# NOTE: sparse code documention due to the repetitiveness of the code
else:
    while (True):
        #presenting the menu to the user and 
        # making sure that the user input is coneverted to lower case.
        menu = input('''\n
Select one of the following Options below:
a - Adding a task
va - View all tasks
vm - View my task
e - Exit

: ''').lower()
        
        # Addition of new tasks
        if (menu == 'a'):
            add_task()


        # Viewing of all tasks regardless of user specificity
        if (menu == 'va'):
            view_all()


        # Viewing of user specific tasks
        elif (menu == 'vm'):
            view_mine()

        # option to end the program  
        elif (menu == 'e'):
            print('Goodbye!!!')
            exit()

        else:
            print("You have made a wrong choice, Please Try again")

