#function with no argument & no return value.

def printLine():
     print("*"*60)

printLine()
print("Welcome to user defined function using python.")
printLine()

#function with Argument but no return value.

def add(a,b):
    print("Addition :",a+b)



printLine()
add(10,20)
printLine()

#function with Argument & return value.

def sub(a,b):
    return a-b

printLine()
#ans=sub(10,20)
print(" subtraction :",sub(23,11))
printLine()



