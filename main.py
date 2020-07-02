# 
# Data Representation One
#
# OBJECTIVE
# You have to implement five functions:
# For all functions, you have to change the return value from 0xABAD1DEA
#
# Three ASCII related functions:
# islower(c) - return Boolean if the character parameter is a lowercase character
# isalpha(c) - return Boolean if a character paramater is a alphanumeric character
# tolower(str) - return a string which converts the str parameter to lowercase
#
# You may need to use the Python built-in functions ord() and chr()
# You need to reference the ASCII table online (google man ascii)
#
#
# There are two hex to binary functions
# hexdigittobin() - returns a string to represent the binary of a hex digit. 
# hextobin() - uses the hexdigittobin() to convert a multi-digit hex number to a binary string
#

#
# islower() : Function to return Boolean True if the character parameter is lowercase ASCII
# Parameters:
# c - string to check the first character of
# Return value: integer - the remainder after integer division
# Example: mod (7, 2) will return 1
#

def islower (c) :
    # Implement your function here
    return 0xABAD1DEA  

#
# isalpha()
# 
# Parameters:

#   
def isalpha (c) :
    # Implement your function here
    return 0xABAD1DEA

#
# tolower() () : 
# Parameters:
# number - integer to check if odd
# 
# Return value - Boolean 
# Example: odd (2) will return False, odd (15) will return True
#     
def tolower (str) :
    # Implement your function here
    return 0xABAD1DEA

#
# hexdigittobin () : function to return the boolean value True if the parameter is even and False if the parameter is odd.
# 
# Parameters:
# number - integer to check if odd
# 
# Return value - Boolean
# Example: even (2) will return True, even (15) will return False
#
  
def hexdigittobin (c) :
    # Implement your function here 
    return 0xABAD1DEA

#
# hextobin () : function to concatentate (add together) two strings
# 
# Parameters:
# string1 - first string 
# string2 - second string
# 
# Return value - a string which is string1 added to string2
# Example: cat ("Good", "bye") will return "Goodbye"
#  
def hextobin (str) :
    # Implement your function here 
    return 0xABAD1DEA



#
# !!!!! UNLESS YOU ARE ADDING NEW TEST DO NOT MODIFY CODE BELOW !!!
# !!!!! PROCEED WITH CAUTION !!!!
#


#
# Test data to test the implementation of the functions
#
testdata = [ 
  # function, nargs, arg1, arg2, expected, return type
    (islower, 1, "a", True, type(True))
  
  (hextobin, 1, "A", "1010", (type ("")))
  
]

outof = 18
import markengine

# Run the markengine
score = markengine.mark (testdata, outof)
