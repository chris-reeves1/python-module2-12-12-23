# functions - a block of code that either perform a task or return a value.

#def greet(name):# parameter which takes in arguments 
#    print(f"hi {name}")

#greet("chris")

#def greet_1(first_name, second_name, age):
#    print(f"{first_name} {second_name} is {age}")

#greet_1("john", "smith", 10)

# Better to use return as we can store a value in a variable
# send it a file, print outside of the function.
# printing inside of function limit functionality
# avoid print and input in functions (anythiing that uses command line)

#def greeter(name):
#    return(f"hello {name}")

#x = greeter("chris")

#print(x)


# default arguments

#def greet3(name, age=10): # default args must come as last arguments
#    return(f"{name} is {age}")

#print(greet3("john"))
#print(greet3("john", 20))


# exercise - make a function that does addition of 2 number that we pass as arguments.

#def add_calc(num1, num2):
#    x = num1 + num2
#    return x

#print(add_calc(5,5))


# *args
# if we dont know how many arguments will be passed into function
# add a * before the parameter name
# it will recieve a tuple of arguments

#def fruit_list(*fruits):
#    print("the fruits are: ")
#    for fruit in fruits:
#        print(fruit)

#fruit_list("apple", "orange", "pear")

#def numbers_list(*numbers):
#    for i in numbers:
#        print(i)

#numbers_list(1,2,3,4,5,6,7,8,9)


# keyword arguments kwargs
# send args as key:value pairs - therefore the order does not matter. 
# we define the value when we pass the arguemnts. 

#def fruit_list(fruit1, fruit2, fruit3):
#    print(f"fav = {fruit1}")
#    print(f"2nd fav = {fruit2}")
#    print(f"3rd fav = {fruit3}")

#fruit_list(fruit1 = "apple", fruit3 = "pear", fruit2 = "orange")

# ** kwargs
# if we dont know how many kwargs there will be.

#def fav_food(**food):
#    print("fav food is", food["fruit"], "not", food["dairy"])

#fav_food(dessert = "ice-cream", fruit = "apple", dairy = "cheese")

# passing a list as a arg

#def my_function(food):
#    for x in food:
#        print(x)

#list1 = ["apple", "pear", "orange"]

#my_function(list1)

# format example

name = "john"
age = 20
height = 1.7

#print("my name is {}, i am {}, my height is {} metres".format(name, age, height))

x = "my name is {}, i am {}, my height is {} metres"

print(x.format(name, age, height))







