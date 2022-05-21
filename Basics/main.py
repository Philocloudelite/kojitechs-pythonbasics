import builtins
from pprint import pprint
from pprint import pprint
import os 


#pprint(dir(builtins))

# print("hello world")
# print(len("hello world"))
# print(sum([3,2,6,7,1]))
# print(input("please enter user name"))

#Variable
first_name = "philo"
last_name = "Essien"
age = 90
# print(age)
# print(type(age))
# print(last_name)
# print(type(last_name))
# print(type(first_name))

## the expected output is
## my first name is philo and my last name is Essien and i am 90 years old

#print(f"my first name is {first_name} and my last name is {last_name} and i am {age} years old")
school = "kojitechs"
class_room = "python"
#print(f"my name is philo, and i school in {school}, and i learn {class_room}")


## How to name your variable== avoid using python builtins to name your variable
## variables are case sensitive
## no space in between your variable === use underscore

#Data type (found in builtin functions)
# Builtin Data types
## str == text, figures all in qoutes("")
## int == numbers = (123)
## list [] == ["apple", "banana", "apple"]
## float == (12.3)
## boolean  bool == True or False
## dictionary dic{} == map = {"name": "philo", "age": 90}
## set {} == set_numbers = {1, 2, 3, 4, 5} {"apple", "banan", "cherry"}
## None
## tuple == {"man", "woman", "land"}

#diff btwn data type and tuple
#print(list_parts[0])

 
# list_parts = {"man", "woman", "land"}
# print(dir(list_parts))

# list_man = ("man", "woman", "land")
# print(dir(list_man))

# #operations
# hello = "hello world"
# print(dir(hello))

# num = 1
# print(dir(num))

# ## Basic calculator
# hello = "hello world!"
# print(type(hello))

# ##print(int(hello)) # we cant convert a string to an interger

# x = 45
# y = str(x)
# print(type(x))
# print(y, type(y))

# ## convert an in to str
# num = 24
# print(type(num))

# conver_to_string = str(num)
# print(type(conver_to_string))

# ## convert a float to an int
# y = 12.2
# print(type(y))

# z = int(y)
# print(type(x))

# ## convert an int to a float
# j = 12
# print(type(x))

# k = float(j)
# print(type(k))

# ## convert with boolean
# ## convert a float to a bool

# x = 0.5
# print(x, type(x))

# y = bool(x)
# print(type(y))

# ## Built basic calculators




name = "Hello world!"
#print(name[0])

#pprint(dir(name))
# name = "Hello world!"
# name.index('w')
# print(name)
# y = "HELLO"
# print(y)

# y.isupper()
# name.rpartition("hello world!")


#name = input("Enter name:")
#print(name)

#name = str(input("Enter name:"))
#print(type(name))

my_dict = {"name": "philo", "country": "Cameroon", "age": 24, "sex": "female"}
#pprint(dir(my_dict))
#print(my_dict.fromkeys())
print(my_dict.get("name"))
contries = my_dict.get("country")
print(my_dict.items())


## tuple dict
tuple_dict = my_dict.items()
for key in my_dict.items():
    print(key)

print(my_dict.keys())


