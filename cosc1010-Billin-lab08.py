# Kaden Billin
# UWYO COSC 1010
# 11-10-24
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 


def check():
    thing = input("Enter a string here: ")
    if (thing).isdigit() == True:
        print("This string is an integer.")
        return int(thing)
    elif thing.split(".")[0].isdigit() and thing.split(".")[1].isdigit():
        split = (thing.split("."))
        if (split[0].isdigit() == False or split[1].isdigit() == False) or len(split) > 2:
            return False
        else:
            print("This string is a float.")
            return float(thing)
    else:
        return False

thing = check()

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

print("Please enter the prompted values below.")

while True:
    m = float(input("enter slope: "))
    b = float(input("enter y-intercept: "))
    xlower = (input("enter lower x bound: "))
    xupper = (input("enter upper x bound: "))
    exit_confirm = input("type 'exit' to exit or 'repeat' to re-enter these values: ")
    if exit_confirm.lower() == "exit":
        break
    elif exit_confirm.lower() == "repeat":
        print("Repeating...")
    else:
        print("This is not one of the accepted responses. This part will be repeated.")


def slope_intercept(m, b, xlower, xupper):
    if xlower.isdigit() == True and xupper.isdigit() == True and int(xupper) >= int(xlower):
        xlower = int(xlower)
        xupper = int(xupper)
        yy = [m * x + b for x in range(xlower, xupper + 1)]
        return yy
    else:
        return False

cc = slope_intercept(m, b, xlower, xupper)
print(cc)

print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

while True:
    aaa = (input("enter a: "))
    bbb = (input("enter b: "))
    ccc = (input("enter c: "))
    exit_confirm = input("type 'exit' to exit or 'repeat' to re-enter these values: ")
    if exit_confirm.lower() == "exit":
        break
    elif exit_confirm.lower() == "repeat":
        print("Repeating...")
    else:
        print("This is not one of the accepted responses. This part will be repeated.")

def checkaaa():
    if (aaa).isdigit() == True:
        return int(aaa)
    elif aaa.split(".")[0].isdigit() and aaa.split(".")[1].isdigit():
        splitaaa = (aaa.split("."))
        if (splitaaa[0].isdigit() == False or splitaaa[1].isdigit() == False) or len(splitaaa) > 2:
            return False
        else:
            return float(aaa)
    else:
        return False

def checkbbb():
    if (bbb).isdigit() == True:
        return int(bbb)
    elif bbb.split(".")[0].isdigit() and bbb.split(".")[1].isdigit():
        splitbbb = (bbb.split("."))
        if (splitbbb[0].isdigit() == False or splitbbb[1].isdigit() == False) or len(splitbbb) > 2:
            return False
        else:
            return float(bbb)
    else:
        return False

def checkccc():
    if (ccc).isdigit() == True:
        return int(ccc)
    elif ccc.split(".")[0].isdigit() and ccc.split(".")[1].isdigit():
        splitccc = (ccc.split("."))
        if (splitccc[0].isdigit() == False or splitccc[1].isdigit() == False) or len(splitccc) > 2:
            return False
        else:
            return float(ccc)
    else:
        return False      

aaa = checkaaa()
bbb = checkbbb()
ccc = checkccc()

def quadform():
    disc = bbb**2 - 4 * aaa * ccc
    if disc > 0:
        xone = (-bbb + ((disc) ** 0.5)) / (2 * aaa)
        xtwo = (-bbb - ((disc) ** 0.5)) / (2 * aaa)
        return xone, xtwo
    else:
        return "null"

answ = quadform()
print(answ)