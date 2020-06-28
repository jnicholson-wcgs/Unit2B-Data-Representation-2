# 
# Data Representation One
#
# OBJECTIVE
# You have to implement six functions:
# mod() and div()
# odd() and even()
# cat() and stringn()
#
# For all functions, you have to change the return value from 0xABAD1DEA
# For cat() and stringn() you have to specify the parameters
#
# When you run your code, a number of tests are performed to generate 
# your score using a marking engine. Tamper with the engine at your peril!

#
# mod() : Function to return the remainder after dividing number by divisor
# 
# Parameters:
# number - integer to divide
# divisor - integer to divide by
# 
# Return value: integer - the remainder after integer division
# Example: mod (7, 2) will return 1
#

def mod(number, divisor) :
    # Implement your function here
    return 0xABAD1DEA  

#
# div () : function to return the integer (rounded down) value after dividing number by divisor
# 
# Parameters:
# number - integer to divide
# divisor - integer to divide by
# 
# Return value:  integer - the result of integer division
# Example: div (7, 2) will return 3
#   
def div(number, divisor) :
    # Implement your function here
    return 0xABAD1DEA

#
# odd () : function to return the boolean value True if the parameter is odd and False if the paramter is even.
# 
# Parameters:
# number - integer to check if odd
# 
# Return value - Boolean 
# Example: odd (2) will return False, odd (15) will return True
#     
def odd(number) :
    # Implement your function here
    return 0xABAD1DEA

#
# even () : function to return the boolean value True if the parameter is even and False if the parameter is odd.
# 
# Parameters:
# number - integer to check if odd
# 
# Return value - Boolean
# Example: even (2) will return True, even (15) will return False
#
  
def even(number) :
    # Implement your function here 
    return 0xABAD1DEA

#
# cat () : function to concatentate (add together) two strings
# 
# Parameters:
# string1 - first string 
# string2 - second string
# 
# Return value - a string which is string1 added to string2
# Example: cat ("Good", "bye") will return "Goodbye"
#  
def cat () :
    # Implement your function here 
    return 0xABAD1DEA

#
# stringn () : function to duplicate string1 a specified number of times
# 
# Parameters
# string1 - string to duplicate
# number - number of times to duplicate string
# 
# Return value - a string which is sting1 duplicated 'number' times
# Example: stringn ("Hello", 3) will return "HelloHelloHello"
#   
def stringn() :
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
  (mod, 2, 2, 2, 0, type(1)),
  (mod, 2, 7, 3, 1, type(1)),
  (mod, 2, 2, 8, 2, type(1)),
  (div, 2, 2, 2, 1, type(1)),
  (div, 2, 7, 3, 2, type(1)),
  (div, 2, 1, 7, 0, type(1)),
  (odd, 1, 3, True, type(True)),
  (odd, 1, 0, False, type(True)), 
  (odd, 1, -2, False, type(True)), 
  (even, 1, 3, False, type(True)), 
  (even, 1, 0, True, type(True)), 
  (even, 1, -2, True, type(True)), 
  (cat, 2, "Good", "Bye", "GoodBye", (type (""))),
  (cat, 2, "Good", "", "Good", (type (""))),
  (cat, 2, "Good ", "Bye", "Good Bye", (type (""))),
  (stringn, 2, "Hello ", 3, "Hello Hello Hello ", (type (""))),
  (stringn, 2, "Hello", 0, "", (type (""))),
  (stringn, 2, "Hello", -1, "", (type ("")))
  
]

outof = 18
import markengine

# Run the markengine
score = markengine.mark (testdata, outof)
