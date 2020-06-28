# 
# 
import sys
import inspect
import dis

# Check if a function has been implemented

def implemented (func, testno) :

  code = dis.Bytecode (func)
  for i in code :
    if (i.argval == 0xABAD1DEA) :
      print ("FAIL: [", testno, "] NOT IMPLEMENTED: ", func.__name__)
      return False
    return True

def runtest (test, testno) :

  res = -1
  passed = True
  func = test[0]
  try: 
    nargs = test[1] 
    if nargs == 0 :
      res = func ()
    elif (nargs == 1) :
      res = func (test[2])
    elif (nargs == 2) :
      res = func (test[2], test[3])
    else :
        print ("MARK ENGINE: [", str (testno), "] Illegal arg count for ", func.__name__)
        passed = False
  
  except:
    print("FAIL: [", testno, "] EXCEPTION: ", func.__name__, sys.exc_info()[0])
    passed = False

  return passed, nargs, res

def markengine () :
  return (mark (testdata))


def mark (data, outof) :

  count = 0
  testno = -1
  for test in data :
    testno += 1
    func = test[0]
    if (not implemented (func, testno)) :
      continue

    if (not inspect.isfunction (func)) :
      print ("FAIL: NOT IMPLEMENTED: ", func.__name__)
      continue

    passed, nargs, res = runtest (test, testno)
    if (passed == False) :
      # Exception or illegal args
      continue
    expected = test[nargs + 2]
    expectedtype = test[nargs + 3]
    if (type (res) != expectedtype) :
      print ("FAIL: [", str (testno), "] RETURN TYPE ERROR: ", func.__name__, "Expected: ", expectedtype, "Got: ", type(res))
    elif (res != expected) :
      print ("FAIL: [", str (testno), "] INCORRECT RETURN VALUE: ", func.__name__, "Expected: ", expected, "Got: ", res)
    else :
      count += 1

  # Print out the score    
  
  percentage = (count / outof) * 100
  print ("\nScore: ", count, "out of", outof, "= ", str(percentage)+"%" )
  return count
