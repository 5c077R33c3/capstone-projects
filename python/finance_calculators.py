import math
# 21/03/2022
# Scott-Reece Morgan
# L1T11: Compulsory Task 1

# A python Program allowing user to access an investment and loan repaymment
# calculator.
#
# Definitions for Simple and compound interest were used from
# LINK : https://www.investopedia.com/articles/investing/020614/learn-simple-and-compound-interest.asp

# The program displays a message asking the user to input his/her selection
print("Select either 'Investment' or 'Bond' from the menu below to proceed:")
print("""\nInvestment     - To calculate your return on investment at a given
                 interest rate.
Bond           - To calculate the amount you'll have to repay on a
                 home loan.""")
selection = input("\nEnter your selection:\t")

# Based on the selection , the program will ask the user to provide information
# used to calculate either the return on investment or to calculate the loan
# repayment amount. This is done using an if-elif-else statement with
# appropriate conditions. if no condition is met , the program asks the user
# to restart the program and try again.

if (selection=="Investment" or selection=="investment" or
    selection=="INVESTMENT"):
    # Investments are calulated using coumpound or simple interest formulas:
    # Compound :   A = P*(1+r)^t
    # Simple   :   A = P*(1+r*t)
    # where
    # A = is the total amount after added interest
    # NOTE: other variables defined in input arguments
    #
    # The user is requested to input the needed information
    print("\nPlease provide the following information.")
    P = float(input("The amount of money you are depositing : R "))
    r = float(input("The interest rate (without the % sign) :   ")) / 100.00
    t = int(input("The term of your investment in years   :   "))
    
    # The user is requested to select between Compound and Simple interest
    print("\nSelect either 'Compound' or 'Simple' from the menu below.")
    print("""\nCompound    - Is calculated on the principal amount and the
              accumulated interest of previous terms.""")
    print("""Simple      - Is calculated on the principal amount only.""")
    interest = input("\nEnter your Selection:\t")
    
    # Based on variable 'interest' one of 2 calulations are conducted, the first
    # is for compound interest and the second for simple. an else statement is
    # included incase an invalid argument is entered.
    if (interest=="Compound" or interest=="compound" or interest=="COMPOUND"):
        A = round(P*math.pow((1+r), t), 2)
        print(f"\nYour expected return is R{A} after {t} years.")
        
    elif (interest=="Simple" or interest=="simple" or interest=="SIMPLE"):
        A = round(P*(1 + r*t), 2)
        print(f"\nYour expected return is R{A} after {t} years.")
        
    else:
        print("""\nYou've incorrectly entered your selection. Please restart the
          program and try again.""")


elif (selection=="Bond" or selection=="bond" or selection=="BOND"):
      # Bond repayment amount is caluclated using :
      # repayment = (i*P)/(1-(1+i)^(-n))
      # where
      # i = monthly interest rate (The yearly divided by 12 months)
      # NOTE: variables defined in input arguments 
      #
      # The user is requested to input the needed information
      print("\nPlease provide the following information.")
      P = float(input("The present value of the house               \t\t: R "))
      i = float(input("The yearly interest rate (without the % sign)\t\t:   ")
                ) / (100.00*12.00)
      n = int(input("The number of months over which the bond will be repaid :   "))
      
      repayment = round((i*P) / (1 - math.pow(1+i, -n)), 2)
      print(f"\nYou'll have to pay R{repayment} each month for {n} months.")

else:
      print("""\nYou've incorrectly entered your selection. Please restart the
          program and try again.""")
        
