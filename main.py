# 
# Data Representation One
#
# OBJECTIVE
# You have to implement five functions:
# For all functions, you have to change the return value from 0xABAD1DEA
#
# Three ASCII related functions:
# islower(c) - return Boolean if the character parameter is a lowercase character
# isalpha(c) - return Boolean if a character paramater is a alphabet character
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
# Here is an example using ord() and chr()
#
# isdigit()
# Passed a string. Check the first character of the string to see if it in the range
# between '0' and '9'
#
# Returns True if character is a digit, otherwise False
#

def isdigit (c) :
    if (ord (c) >= ord ('0') and ord (c) <= ord ('9')) :
        return True
    else :
        return False

# Test out the isdigit() code with boundary cases and error cases
#
for c in "09185;aA" :
    print ("isdigit() of ", c, "is: ", isdigit (c))

        
#
# islower() : Function to return Boolean True if the character parameter is lowercase ASCII
# Parameters:
# c - string to check the first character of
#
# Return value: True is character is lowercase, False otherwise
# Example: islower ("a) will return True, islower ("A") and islower (";") return False
#

def islower (c) :
    # Implement your function here
    return 0xABAD1DEA  

#
# isalpha()
# 
# Parameters:
# c - string to check the first character of
#
# Check if the character is lower case or upper case character
#
# Return value: True is character passed is upper or lower case, False otherwise
# Example: isalpha ("f"), isalpha ("F") all return True. isalpha ("8") and isalpha ("@") returns False
#

#   
def isalpha (c) :
    # Implement your function here
    return 0xABAD1DEA

#
# tolower() 
# Parameters:
# str - string to convert to lowercase
# 
# Return value - str parameter converted to lowercase
# Example: tolower ("hello) will return "hello", tolower ("HeLLo") will return "hello" and tolower ("H.e.L.l.o") will return "h.e.l.l.o"
#     
def tolower (str) :
    # Implement your function here
    return 0xABAD1DEA

#
# hexdigittobin ()
# 
# Parameters:
# c - hexadecimal character to convert to a binary string
# 
# Return value - binary string representing the hex character. Will return an empty string if character is not a valid hex digit
# Example: hexdigittobin("A") will return "1100", hexdigittobin ("0") will return "0000", hexdigittobin ("G") will return ""
#
  
def hexdigittobin (c) :
    # Implement your function here 
    return 0xABAD1DEA

#
# hextobin () : function to concatentate (add together) two strings
# 
# Parameters:
# str - hexadecimal sting to convert to binary
# 
# Return value - a string representing the binary number for hex striing
# Example: hextobin ("00") will return "00000000", hextobin ("AF") will return "11001111"
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
    (islower, 1, "a", True, type(True)),
    (islower, 1, "B", False, type(True)),
    (islower, 1, ";", False, type(True)),
    (isalpha, 1, "a", True, type(True)),
    (isalpha, 1, "9", False, type(True)),
    (isalpha, 1, "Z", True, type(True)),
    (isalpha, 1, ";", False, type(True)),
    (tolower, 1, "abc", "abc", type("")),
    (tolower, 1, "AbC", "abc", type("")),
    (tolower, 1, "A.B.C", "a.b.c", type("")), 
    (hexdigittobin, 1, "A", "1010", type("")),
    (hexdigittobin, 1, "G", "", type("")),
    (hexdigittobin, 1, "f", "1111", type("")),
    (hextobin, 1, "A", "1010", (type (""))),
    (hextobin, 1, "FF", "11111111", (type (""))),
    (hextobin, 1, "F0F", "111100001111", (type ("")))
  
]

outof = 16
import markengine

# Run the markengine
score = markengine.mark (testdata, outof)
