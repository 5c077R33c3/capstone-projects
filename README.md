# capstone-projects
collection of capstone projects from Hyperion Dev bootcamp
## Python
### Capstone I: Finance calculator
A python program allowing a user to access an investment and loan repaymment
calculator. The program is linear and does not use any loops to navigate between different sections, this means if a mistake is made , the program needs to be restarted and the correct values or decisions made.

the goal of this program is to provide an effective way for the inted user to calculate investments or load repayemnts

### Capstone II: Task manager
A modular python program that requires a user to log in to access information regarding assigned tasks.

The program is designed to accomodate two types of users:
 * admin users (are are allowed to add personnell to the system and view statistics of tasks);
 * normal users (arent offered the above mentioned options but have access to all other functionality).

All user input apart form the menu selection is appended to the appropriate
.txt file

The program runs within various while loops under certain conditions that allow the user to navigate between desired sections. This is done using logic that violates or grants the loop condition.

The goal of this program is to provide a way for small to medium businesses to assign and track tasks to all employees. It provides a level of accountability with respect to the completion and handling of tasks.

### Capstone III: Inventory
A modular python program that used to track the amount of stock per item and the value associated with it. The program runs of two main classes:
 * The Warehouse class, which is a child of the list class, this class is used to contain the item and its methods are tailored to required functionality.
 * The Shoe class, this is an item class that creates an object with the set required information for each type of shoe stored in the warehouse.

The main Scripts is divided into two sections using an if-elif flow control.
the functionality of the program caters for two types of users:

 * Global users - These users are allowed to see how stock is distributed
    throughout the globe using the inventory and search options they are given.
    The inventory gives the options to view the highest and lowest stocked
    products for each region.
    The search option allows the global user to search according to product,
    code or country. For each option the total quantity and value is given for
    the all the stock related to that search, ie. all the total value and
    quantity for all the stock in China, if china is searched.

 * Regional users - These users are allowed to see how stock is distributed
    in their respective regions.
    Through the inventory option they are allowed to view and edit the class
    instance variables for the the object with the highest and lowest quantity.
    Through the search option they are allowed to search for shoe objects by code.

The Program is designed so that the Regional users have an idea of how their assets are distributed within the region and Global users have the same idea , but on a much larger scale.


## Java
### Capstone I: Application (Poised)
Is an OOP Project management system that can create, update and track projects for a structural engineering firm. The entire program is run from the Appliction class, with calls to other classes when when certain actions are carried out.
Whenever a finalization occurs the program reccurs to the Apllication class, this happens until the program is closed.

The program is designed to be accessed by individual users overseeing data capturing or incharge of administrative duties and provides a neat and effective what of storing and managing stored data (Projects, Clients, Architects and Contractors).
