# 
# Data Representation One
#


def task1() :
    return 0xABAD1DEA  
    
def task2() :
    return 0xABAD1DEA
    
def task3() :
    return 0xABAD1DEA
    
def task4() : 
    return 0xABAD1DEA

def task5() :
    return 0xABAD1DEA

import markengine

testdata = [ 
  # function, nargs, arg1, arg2, expect
  (task5, 0, 2, type(1)),
  (task1, 1, 3, 1, type(1)), 
  (task1, 1, 2, 1, (type (""))),
  (task1, 1, 2, 2, (type (1))),
  (task2, 1, 1, 2, type (1)),
  (task2, 1, 4, 8, type (1)),
  (task3, 1, "Hello", 4, type(1)),
  (task4, 1, "Hello", 4, type(1))
]

# Run the markengine
score = markengine.mark (testdata)
