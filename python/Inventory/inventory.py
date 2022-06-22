# 15/05/2022
# Scott-Reece Morgan
# L1T29: Capstone project IV

from tabulate import tabulate
import os
from operator import itemgetter

# Reference
# sorting asingle column of a 2d array https://stackoverflow.com/questions/11287207/why-should-i-use-operator-itemgetterx-instead-of-x/11287216#11287216

#                                FUNCTIONS

# A function to write passed information to a .txt file using a for loop and
# the write function.
def write_to_file(filename, object_list):
     """A function to write data to a .txt file"""
     
     header = "Country,Code,Product,Cost,Quantity,Value"
     with open(filename, 'w+', encoding = 'utf-8') as file:
          file.write(header + "\n")
          for obj in object_list:
           file.write(f"{obj.country},{obj.code},{obj.product},{obj.cost},{obj.quantity},{obj.value}\n")

     return 

# A function calculating the value of the total stock of a shoe, the function
# then updates the value class variable.
#
# The function accepts two parameters , the first , the index of the object
# the second is a boolean to determine whther the vaule should be passed to
# the main cripts or not.

def value_per_item(index, assign = True):
     """A function calculating the value of an item and adjusting the object
        information.

        value = quantity * cost"""
     # Assignment to main script is needed
     if (assign == True):
          value = warehouse[index].cost * warehouse[index].quantity
          warehouse[index].value = value
          return value
     
     # Assignment to main script is not needed
     else :
          value = warehouse[index].cost * warehouse[index].quantity
          warehouse[index].value = value
          return          

#                                 CLASSES

class Shoe(object):
     """The shoe class creates an object for a quasi unique item, where the
        product may be the same but all or some other properties may differ.
        Therefore each obeject can be identified as a single item, or identified
        as part of a group.

        eg. all objects from the country South Africa can be grouped together in
        a search, or all air maxes across different regions can be found"""

     value = None

     # Constructor
     def __init__(self, country, code, product, cost, quantity):
         self.country = country
         self.code = code
         self.product = product
         self.cost = float(cost)
         self.quantity = float(quantity)


class Warehouse(list):
     """The 'global' warehouse object is designed to keep track of inventory stored
        in many different regions and is a subclass of the list parent class.

        The Methods:
          > read_data() populates the warehouse object from a user .txt file
            by creating shoe objects from the dat read in the .txt file
            and appending the object to the warehouse

          > search() locates shoe objects by reqion , product and code, allowing
            all items in the warehouse for a particular region or product to be
            seen whereas search by code only returns a single object unique to
            that code.

          > lowest(self, region) searches the warehouse fro the object with the
            lowest quantity. The method accepts an additional argument 'region'
            if theis value is passed, the object with the lowest quantity is found
            only for that region.

          > highest(self, region) searches the warehouse fro the object with the
            highest quantity. The method accepts an additional argument 'region'
            if theis value is passed, the object with the highest quantity is found
            only for that region.
             """
     regions = []

     # Constructor
     def __init__(self):
        super().__init__(self)


     # METHODS
     # Read data
     # as the file is read using a for loop, the information from the read file
     # is split into a temporary list. The items in that list is then used to
     # populate the warehouse with shoe objects
     def read_data(self):
          with open('inventory.txt', 'r', encoding = 'utf-8') as file:
               
               # The first line of the .txt file is ignored
               # all other lines are read.
               for index, line in enumerate(file):
                    if (index == 0):
                         pass

                    else:
                         temp = line.strip().replace("\n", "").split(",")
                         shoe = Shoe(temp[0], temp[1], temp[2], temp[3], temp[4])
                         self.append(shoe)
                         value_per_item(index - 1, False)
                         if (temp[0] in self.regions):
                              pass
                         
                         else:
                              self.regions.append(temp[0])

     # Lowest
     # Governed by an if-elif flow control to determine whether the search
     # conducted should be a regional or global search.
     #
     # In each branch runs a for loop that iterates through the warehouse items
     # insearch of the product with the lowest quantity. Each items index and
     # quantity is stored in a temporary list, the lowest from the region is
     # found using the min fuction and appended to the 'lowest' list.
     #
     # In the case of no region being passed to the method, the above for loop
     # is run within a for loop iterating through a list of regions.
     #
     # The lowest list is then printed to the terminal
     def lowest(self, region = None):
          lowest = []

          if (region is None):

               # Iterating though list of regions
               for country in self.regions:
                    temp = []
                    # iterating through warehouse
                    for index, product in enumerate(self):
                         if (country == product.country):
                               temp.append([index, product.quantity])

                    lowest.append(min(temp, key = itemgetter(1)))

               # Printing of list
               for item in lowest:
                    print(f"""
[{item[0]}]. {self[item[0]].product}
\tcode : {self[item[0]].code}
\tqnty : {self[item[0]].quantity}
\tcntry: {self[item[0]].country}
\tcost : {self[item[0]].cost}""")


          elif (region is not None):
               temp = []
               # iterating through warehouse
               for index, product in enumerate(self):
                    if (region == product.country):
                         temp.append([index, product.quantity])

               lowest.append(min(temp, key = itemgetter(1)))

               # Printing of list
               for item in lowest:
                    print(f"""
[{item[0]}]. {self[item[0]].product}
\tcode : {self[item[0]].code}
\tqnty : {self[item[0]].quantity}
\tcntry: {self[item[0]].country}
\tcost : {self[item[0]].cost}""")

               return lowest[0][0]

     # Highest
     # Governed by an if-elif flow control to determine whether the search
     # conducted should be a regional or global search.

     # In each branch runs a for loop that iterates through the warehouse items
     # insearch of the product with the highest quantity. Each items index and
     # quantity is stored in a temporary list, the lowest from the region is
     # found using the max fuction and appended to the 'highest' list.
     #
     # In the case of no region being passed to the method, the above for loop
     # is run within a for loop iterating through a list of regions.
     #
     # The highest list is then printed to the terminal
     def highest(self, region = None):
          highest = []

          if (region is None):

               # Iterating through list of regions
               for country in self.regions:
                    temp = []
                    # Iterating through warehouse
                    for index, product in enumerate(self):
                         if (country == product.country):
                               temp.append([index, product.quantity])

                    highest.append(max(temp, key = itemgetter(1)))

               # Printing of list
               for item in highest:
                    print(f"""
[{item[0]}]. {self[item[0]].product}
\tcode : {self[item[0]].code}
\tqnty : {self[item[0]].quantity}
\tcntry: {self[item[0]].country}
\tcost : {self[item[0]].cost}""")


          elif (region is not None):
               temp = []
               # Iterating through warehouse
               for index, product in enumerate(self):
                    if (region == product.country):
                         temp.append([index, product.quantity])

               highest.append(max(temp, key = itemgetter(1)))

               # Printing of list
               for item in highest:
                    print(f"""
[{item[0]}]. {self[item[0]].product}
\tcode : {self[item[0]].code}
\tqnty : {self[item[0]].quantity}
\tcntry: {self[item[0]].country}
\tcost : {self[item[0]].cost}""")

               return highest[0][0]


     # Search
     def search(self, search_value, checking = False):

          inventory = []
          value = 0
          quantity = 0

          # With each iteration through self , the item is checked against various
          # object properties using and If-elif flow control. once the codition is
          # passed the object information is stored in a list then appended to the
          # main inventory list for printing. An extra bit of information is generated
          # called value , this is the total value of all the stock in that category.
          # this is also added to the sub-list.
          for index, item in enumerate(self):
               # Search according to Region
               if(item.country == search_value):
                    inventory.append([item.country, item.code, item.product,
                                      item.cost, item.quantity,
                                      item.value])
                    value += item.value
                    quantity += item.quantity

               # Search according to product
               elif(item.product == search_value):
                    inventory.append([item.country, item.code, item.product,
                                      item.cost, item.quantity,
                                      item.value])
                    value += item.value
                    quantity += item.quantity

               # Search according to item code
               elif(item.code == search_value):
                    inventory.append([item.country, item.code, item.product,
                                      item.cost, item.quantity,
                                      item.value])
                    value += item.value
                    quantity += item.quantity

          # if an invalid entry is entered and no items match , then a custom
          # error is raised to notify the user of an invalidity. Otherwise the
          # list is tabulated and printed.
          #
          # This is done using if-else flow control to check the length of the
          # inventory list.
          if (checking == False):
               if (len(inventory) == 0):
                    raise NoMatchError

               else:
                    print(f"""Inventory
Total quantity : {quantity}
Total value    : {value}
""")
                    print(tabulate(inventory, headers = ["Country", "Code", "Product", "Cost", "Quantity", "Value"]))

          else:
               if (len(inventory) == 0):
                    raise NoMatchError

               else:
                    return search_value

# Custom exception class to show that no items are matched
class NoMatchError(Exception):

     pass


#                                 SCRIPT

# Object declaration and initialization
warehouse = Warehouse()
warehouse.read_data()
out = False
action = ""

# The main Scripts is divided into two sections using an if-elif flow control.
# the functionality of the program caters for two types of users:
#
# > Global users - These users are allowed to see how stock is distributed
#    throughout the globe using the inventory and search options they are given.
#    The inventory gives the options to view the highest and lowest stocked
#    products for each region.
#    The seach option allows the global user to search according to product,
#    code or country. For each option the total quantity and value is given for
#    the all the stock related to that search, ie. all the total value and
#    quantity for all the stock in China , if china is searched.
#
# > Regional users - These users are allowed to see how stock is distributed
#    in their respective regions.
#    Through the inventory option they are allowed to view and edit the class
#    instance variables for the the object with the highest and lowest quantity.
#    Through the search option they are allowed to search for shoe objects by code.
while (True):
     # Login in as a Regional warehouse manager or as a Global warehouse manager.
     level = input("""Welcome to the Nike Warehouse database!
To which Warehouse level do you belong?

Global
Regional

Response : """).strip().lower()

     # Global flow control
     if (level == "global"):

          while (True):

               # Main menu
               menu = input("""
Please select what you would like to do.

Inventory
Search

Response : """).strip().lower()

               # Action for inventory and all sub-actions
               if (menu == "inventory"):
                    
                    
                    while (action != "home"):
                         out = False
                         option = input("""
Would you like to:

View lowest
View highest

Response : """).lower().strip()

                         # View lowest
                         if (option == "view lowest"):
                              
                              while (out == False):
                                   # Retriving and printing lowest values
                                   warehouse.lowest()

                                   # End of page action to move between menues
                                   while (True):
                                        action = input("""

Return
Home

Response : """).strip().lower()
                                        if (action == "home"):
                                             menu = ""
                                             option = ""
                                             out = True
                                             break

                                        elif (action == "return"):
                                             option = ""
                                             out = True
                                             break

                                        else:
                                             print("Oops, Please enter the resopnse as you see it.")

                         
                         # View highest
                         elif (option == "view highest"):
                              
                              while (out == False):
                                   # Retrieving and printing highest values
                                   warehouse.highest()

                                   # End of page action to move between menues
                                   while (True):
                                        action = input("""
Return
Home

Response : """).strip().lower()

                                        if (action == "home"):
                                             menu = ""
                                             option = ""
                                             out = True
                                             break

                                        elif (action == "return"):
                                             option = ""
                                             out = False
                                             break

                                        else:
                                             print("Oops, Please enter the resopnse as you see it.")

                         else:
                              input("You have entered an invalid entry, press enter to retry.")

               
               # Action for search
               elif (menu == "search"):

                    # Searching according to Region, Product, or code
                    while (True):
                         # try-except block handling search action using the search
                         # method, but also controlling the exit code and the Exception
                         # if no search is found(ie. an invalid entry)
                         try :
                              warehouse.search(input("Search Region/Product/Code :\t").strip())
                              action = input("""\nReturn to main menu - home
Search new item - search
\nAction:\t""").strip().lower()

                              if (action == "home"):
                                   action = ""
                                   menu = ""
                                   break

                              elif (action == "search"):
                                   pass

                              else :
                                   print("\nPlease enter a correct action.")


                         except NoMatchError:
                              temp = input("""Your search does not match any item in the warehouse.

Press enter to retry.""")


               else:
                    print("Something went wrong, please enter the response as you see it.")
               
               write_to_file("inventory.txt", warehouse)


     elif (level == "regional"):

          # utilizing a while loop to search if the region entered has items in the warehouse.
          # if no item is found then the NoMatchError is raised.
          while (True):
               try :
                    region = warehouse.search(input("Please enter your Region : ").strip(), checking = True)
                    break

               except NoMatchError :
                    print("Sorry! No Nike warehouse found in that region, please enter a valid region")

          while (True):
               # main menu
               menu = input("""
Please select what you would like to do.

Inventory
Search

Response : """).strip().lower()

               # Action if inventory and all sub-actions 
               if (menu == "inventory"):

                    while (action != "home"):
                         out = False
                         option = input("""
Would you like to:

Restock lowest
Markup highest

Response : """).lower().strip()

                         # Restock lowest
                         # After choosing to restock lowest, the user is prompted to select
                         # the index number of the stock item theyd like to restock. The
                         # index is then used to adjust the quantity of the chose object.
                         # The value is then adjusted using the value per item function
                         if (option == "restock lowest"):

                              while (out == False):
                                   # Retrieving the lowest for the entered region
                                   lowest_index = warehouse.lowest(region)
                                   try :
                                        restock = input("""
Restock Product

Yes/No : """).strip().lower()
                                        if (restock == "yes"):
                                             increment = int(input("Increase stock by (number): "))
                                             warehouse[lowest_index].quantity += increment
                                             value_per_item(lowest_index, False)

                                        elif (restock == "no") :
                                             # End of page action
                                             while (True):
                                                  action = input("""
Restock
Return
Home

Response : """).strip().lower()

                                                  if (action == "home"):
                                                       menu = ""
                                                       option = ""
                                                       out = True
                                                       break

                                                  elif (action == "return"):
                                                       option = ""
                                                       out = True
                                                       break

                                                  elif (action == "restock"):
                                                       break

                                                  else :
                                                       print("Oops, Please enter the resopnse as you see it.")

                                        else :
                                             print("Oops, Please enter the resopnse as you see it.")

                                   
                                   except ValueError:
                                        input("You have entered an invalid value, press enter to retry.")

                         
                         # After choosing to markup highest, the user is prompted to select
                         # the index number of the stock item theyd like to markup. The
                         # index is then used to adjust the cost of the chose object.
                         # The value is then adjusted using the value per item function
                         elif (option == "markup highest"):

                              while (out == False):
                                   highest_index = warehouse.highest(region)
                                   try :
                                        markup = input("""
Mark up item for sale?

Yes/No : """).strip().lower()
                                        if (markup == "yes"):
                                             reduction = float(input("""
Enter the percent reduction on cost for the product : """).strip().replace("%", ""))
                                             warehouse[highest_index].cost = warehouse[highest_index].cost * ((100 - reduction) / 100)
                                             value_per_item(highest_index, False)

                                        elif (markup == "no"):
                                             # End of page action
                                             while (True):
                                                  action = input("""
Markup
Return
Home

Response : """).strip().lower()

                                                  if (action == "home"):
                                                       menu = ""
                                                       option = ""
                                                       out = True
                                                       break

                                                  elif (action == "return"):
                                                       option = ""
                                                       out = True
                                                       break

                                                  elif (action == "markup"):
                                                       break

                                                  else:
                                                       print("Oops, Please enter the resopnse as you see it.")

                                        else :
                                             print("Oops, Please enter the resopnse as you see it.")
                                                  

                                   except ValueError:
                                        input("You have entered an invalid value, press enter to retry.")
                         
                         
                         else :
                              input("You have entered an invalid entry, press enter to retry.")

               # Action for search
               elif(menu == "search"):

                    # To search according to code
                    while (True):
                         # try-except block handling search action using the search
                         # method, but also controlling the exit code and the Exception
                         # if no search is found(ie. an invalid entry)
                         try :
                              warehouse.search(input("Search Code :\t").strip())
                              action = input("""\nReturn to main menu - home
Search new item - search
\nAction:\t""").strip().lower()

                              if (action == "home"):
                                   action = ""
                                   menu = ""
                                   break

                              elif(action == "search"):
                                   pass

                              else :
                                   print("\nPlease enter a correct action.")
                                   

                         except NoMatchError:
                              input("""Your search does not match any item in the warehouse.

Press enter to retry.""")

               
               else:
                    print("Something went wrong, please enter the response as you see it.")
               
               write_to_file("inventory.txt", warehouse)
               

                    
     else:
          print("Something went wrong, please enter the level as you see it.")
