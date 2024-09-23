def function1():
  print("hello world , this is the execution of the first funtion !")
  function2() #calling function2 inside function1
  
def function2():
  print("and this is the execution of the second funtion !!");


if __name__ == "__main__": #when executing python3 file.py , the python will set __name__ (variable) to "__main__" (value) 
  function1()
