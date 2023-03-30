# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import os
def printMenu():
    '''
    prints a menu that outlines what users can input and where it will direct them
    '''
    print("Customer and Sales System\n 1. Enter Customer Information\n 2. Generate Customer data file\n 3. Report on total Sales (Not done in this part)\n 4. Check for fraud in sales data (Not done in this part)\n 9. Quit\nEnter menu option (1-9)")
          

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def enterCustomerInfo():
    '''
    Asks the user for their Firstname, Last Name, City, Postal code then runs the function to validate it, and credicard and runs the function to valdiate it.
    '''
    print("Input your first name")
    fname = input("> ")
    while fname =="":
        print("This is a required field, please do not leave blank.")
        fname = input("> ")
    print("Input your last name")
    lname = input("> ")
    while lname == "":
        print("This is a required field, please do not leave blank.")
        lname = input("> ")
    print("Input your city")
    city = input("> ")
    while city=="":
        print("This is a required field, please do not leave blank.")
        city = input("> ")
    print("Input Postal Code")
    postal = input("> ")
    while validatePostalCode(postal) == False:
        print("Your Postal Code was not valid, please try again.")
        postal = input("> ")
    print("Valid Postal Code")
    print("Input Credit Card")
    ccard = int(input("> "))
    while validateCreditCard(ccard) == False:
            print("Your credit card was not valid, please try again")
            ccard = int(input("> "))
    print("Credit Card accepted")
    return fname,  lname, city, postal, str(ccard)
    

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validatePostalCode(postal):
    '''
    Checks if the postal code inputted by the user is valid
    '''
    folder = os.getcwd()
    filename = folder + "\\Wong Riley LuhnAlgorithnm\\postal_codes.csv"
    file = open(filename, "r")
    line = file.readlines()
    a = len(line)
    if len(postal)<3:
        return False
    else:
        for i in range(1, a):
            currentLine = (line[i])
            currentPostal = currentLine[:3]
            if postal[:3]== currentPostal:
                return True
            else:
                continue
        file.close
        return False    
'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validateCreditCard(num):
    '''
    Checks whether the credit card inputted by the user is valid
    '''
    sum1 = 0
    sum2 = 0
    reverse = str(num)[::-1]
    length = len(reverse)
    if length < 9 or length >16:
        return False
    else:
        for i in range(length):
            if i%2 == 0:
                sum1 += int(reverse[i])
            else:
                digit = 0
                double = int((reverse[i])) * 2
                doublestr = str(double)
                lendouble = len(doublestr)
                if int(double) > 9:
                    for x in range(lendouble):
                        digit += int(doublestr[x])
                else:
                    digit = double
                sum2 += digit
        total = sum1 + sum2 
        if total % 10 == 0:
            return True
        else:
            return False 

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def generateCustomerDataFile():
    '''
    Creates a file if there is not already one already, if there is one, adds the customer info to it. 
    '''
    from os.path import exists
    folder = os.getcwd()
    filename = folder + "\\Wong Riley LuhnAlgorithnm\\Users.csv"
    fileExists = exists(filename)
    fname, lname, city, postal, ccard= info
    if fileExists == False:
        file = open(filename, "w")
        file.writelines("ID | First Name | Last Name | City | Postal Code | CreditCard\n")
        file.writelines("1 | "+ fname +" | " + lname+" | " + city+" | " + postal+" | " + ccard+" | " +  "\n")
        file.close
    elif fileExists == True:
        file = open(filename, "r")
        line = file.readlines()
        lineCount = int(len(line))
        file.close
        file = open(filename, "a")
        id = str(lineCount) + " | "
        file.writelines(id + fname+" | " + lname+" | " + city+" | " + postal+" | " + ccard+" | " + "\n")
        file.close

    #fileName = folder + "\\python\\Wong Riley LuhnAlgorithnm\\Users\\" + str(count) + ".text"
    #file = open(fileName, "w")
    #file.writelines(enterCustomerInfo())

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = 1
generateCustomerOption = 2
exitCondition = 9

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = int(input(">: "));        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        info = enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile()
        print("User has been added")
    elif userInput == exitCondition:
        exitCondition = 9
    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")