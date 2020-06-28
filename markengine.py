# 
# 
import sys
import inspect
import dis

# Check if a function has been implemented

def implemented (func, t) :

  fcall = func.__name__ + "()"
  code = dis.Bytecode (func)
  for i in code :
    if (i.argval == 0xABAD1DEA) :
      print (t, "NOT IMPLEMENTED: ", fcall)
      return False
    return True

def runtest (test, t) :

  res = -1
  passed = True
  func = test[0]
  fcall = func.__name__ + "()"
  try: 
    nargs = test[1] 
    if nargs == 0 :
      res = func ()
    elif (nargs == 1) :
      res = func (test[2])
      fcall = func.__name__ + '(' + str (test[2]) + ")"
    elif (nargs == 2) :
      res = func (test[2], test[3])
      fcall = func.__name__ + "(" + str (test[2]) + ", " + str(test[3]) + ")"
    else :
        print ("{} MARK ENGINE: Illegal arg count for {}".format (t, func.__name__))
        passed = False
  
  except:
    print("{} RUNTIME EXCEPTION: {} {}".format (t, func.__name__, sys.exc_info()[0]))
    passed = False

  return passed, nargs, res, fcall

def markengine () :
  return (mark (testdata))


def mark (data, outof) :

  count = 0
  testno = -1
  for test in data :
    testno += 1
    func = test[0]
    t = "FAILED TEST [" + str(testno) + "]: "
    if (not implemented (func, t)) :
      continue

    if (not inspect.isfunction (func)) :
      print ("{} NOT IMPLEMENTED: {}()".format (t, func.__name__))
      continue

    passed, nargs, res, fcall = runtest (test, t)
    if (passed == False) :
      # Exception or illegal args
      continue
    
    expected = test[nargs + 2]
    expectedtype = test[nargs + 3]
    
    if (type (res) != expectedtype) :
      print ("{} RETURN TYPE: called {}: Expected: {}, Got: {}".format (t, fcall, expectedtype, type(res)))
    elif (res != expected) :
      print ("{} RETURN VALUE: called {}: Expected: {}, Got: {}".format (t, fcall, expected, res))

    else :
      count += 1

  # Print out the score    
  
  percentage = (count / outof) * 100
  print ("\nScore: ", count, "out of", outof, "= ", str(percentage)+"%" )
  return count

