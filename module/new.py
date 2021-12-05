'''

import cal
import other
   #it means importing all the file of cal module
print(cal.add(2,4))
print(cal.subtract(2,4))
print(other.sqr(2))


# the form of statement
from cal import add,subtract
from other import sqrt

a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(add(a,b))
print(subtract(a,b))
print(sqrt(a))

# Importing and renaming module
import other as o
print(o.sqr(3))




from typing import Protocol
from cal import *
from other import *

a=add(3,4)
print(a)
b=subtract(4,5)
print(b)
c=sqr(4)
print(c)


The dir() function
#taking all thge file or functin of the module 
import math,random
import other
import cal
print(dir(cal))


# math Module
import math
r=float(input("Enter the radius of circle"))
a=math.pi
print(a*r*r)

# Finding the ceiling and the floor value
import math
a=float(input("Enter the valuue of a:"))
b=float(input("Enter the valuue of b:"))
print(math.ceil(a))
print(math.floor(b))



# Finding the factorial of the number
import math
a=int(input("Enter the value  of a which you want to find factorail of that numbe:"))
print(f"the factorial of {a} is:")
print(math.factorial(a))

# Finding the GCD
import math
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(f"the gdc of {a} and {b} is:")
print(math.gcd(a,b))

# Finding the absolute value
import math
a=int(input("Enter the valu eof a:"))
print(f"the absolute value of {a} is :")
print(math.fabs(a))



# Finding the power of a number
import math
print(math.pow(3,4))



# Finding the Logarithm
import math
print(math.log(10,10))



# Finding the Square root
import math
import math

# print(math.sqrt(4.6))
print(math.sqrt(857))
# Finding sine, cosine, and tangent

import math
a=math.pi/6
print(math.sin(a))
print(math.cos(a))
print(math.tan(a))

# Converting values from degrees to radians and vice
# versa


import math
a=math.pi/6
b=30
print(math.degrees(a))
print(math.radians(a))



# isnan() method
import math
print(math.isnan(75))
print(math.isnan(float("nan")))



# random module

import random
l=[1,2,3,4,6]
print(random.choice(l))


# random.choice()
import random


# l=[1,2,3,4,"khushilal"]  #accessing from the list
# print(random.choice(l))

l2=(1,2,3,456,78)
print(random.choice(l2))

import random
a="python"
print(random.choice(a))

import random 
a=random.randint(2,6)
print(f"the randome number between 2 and 6 be: {a}")


# random.shuffle()
import random
l=[1,2,3,4.5,6,7,8]
print(f"the list before shuffle be:{l}")
a=random.shuffle(l)
print(f"the list after the suffle be:{l}")

'''

# # random.seed( )
# import random
# print(random.randint(1,20))
# print(random.seed(3))

from random import sample
l=[1,2,3,4]
print(sample(l,2))