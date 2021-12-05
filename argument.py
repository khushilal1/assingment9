# Arguments of a Function

def oddeven(x):    #oddeven function return that value the given instruction is used
    if x%2==0:
        print(f"the entered number: {x} is even number:")
    else:
        print(f"The entered number {x} is odd number")
y=int(input("Enter the value of y:"))
oddeven(y)
oddeven(y)



y=int(input("Enter the value of y:"))
def oddeven(x):    #oddeven function return that value the given instruction is used
    if x%2==0:
        print(f"the entered number: {x} is even number:")
    else:
        print(f"The entered number {x} is odd number")
oddeven(y)
oddeven(y)

# Types of arguments


# 1. Default arguments
def add(a=5,b=4):  #add is a default argumrntwhose value is define inside the  user defined
    print(a+b)
add(3,5)

def add(a=5,b=4):  #add is a default argumrntwhose value is define inside the  user defined
    print(a+b)
add()    #by default in case not the value is not keep in calling function the functionus


def display(x=5,y=7):
    print("the value of x:",x)
    print("the value of y:",y)
display(  4,8)


def display(y=5,x=7):
    print("the value of y:",y)
    print("the value of x:",x)
display(3)



# 2. Keyword arguments
def display(x,y):
    print(f"the value of x:{x}")
    print(f"the value of x:{y}")
display(x=5,y=10)


def student(firstname,lastname):
    print(firstname,lastname)

a=input("Enter your name:")
b=input("lastname")
student(a,b)


# 3. Variable length argument

# *args (Non-Keyword Arguments)
def b(*a):  #"*" makes the return value in terms of tuple form ehich can be confirmed by using the type function 
    print(a)
    print(type(a))
    print(type(b))
b(1,"khushilal",75865,778,7898,4.5,(3,4,5),[4,5,6,7],"mohan")


def b(**a):  #"**" gives the value in terms of the dictionary which can be  confirmed using the type function
    print(a)
    print(type(a))
b(_1=878654,_2="mohan",_3={2,3,4,5},_4=7567)  #the value must be return in term of the keyword  argument

# 4. Docstring

def evenodd(x): 
     
    if(x%2==0):
        print(f"{x} is even number")
    else:
        print(f"{x} is odd  number")
        evenodd(2)





def evenOdd(x): 
    if (x % 2 == 0):
        print("even")
    else:
      print("odd")

# Driver code to call the function
evenOdd(4)
print(evenOdd.__doc__)