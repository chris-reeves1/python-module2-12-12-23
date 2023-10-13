# variables - a reference (a name), a section of memeory
# protected - cant be altered unless callled by name. Memory reserved.   

#age = 10 
#x = 10

# naming convention - names should be descriptive, lowercase, never start with a number
# pep-8 style guide
# be consistant  

#Var = 10 avoid starting with cap
#1var = 10 dont start with a number
#VAR = avoid all caps
#print = avoid python keywords

#person_one_age = 10 # snake case
#personOneAge = 10 # camel case

# built-in functions:
# print (prints to standard output)
# type (show data type)
# input (allows text input on standard input)
# class (builds a class - OOP)

# data types:

#x = 10 # int = integer - whole numbers
#y = "10" # string - words, paragraphs etc
#z = True # Bool - true or false (0/1, something or nothing)
#v = 1.03 # float - decimal number 

#print(type(v))

#name = input("what is your name?") # input defaults to string 
#age = int(input("what is your age?"))

#print("your name is" + " " + name)
#print("your name is", name)
#print(f"your name is {name}, your {age} years old!") # f string - use different data types in a printed string


#name = "rex"
#age = 3
#bark = True
#meow = False

#print("statement:", name, "barks:", bark)

# escape characters
# \\ backlash, \"string here\", \n new line, \t tab, \u unicode, \U extended unicode.   

# print("person 1: \tHey how are you?\nPerson 2: \tGood thanks! \U0001F604")

# stings methods

print("hEllO WorlD".lower())
print("hello world".upper())

print("hello world".replace("world", "class"))

print("hello world".count("o"))
print("hello world".split(","))

# Bodmas

# brackets
# order by (powers) 2**5
# division
# multiplication
# addition
# subtraction 

# regular maths symbols + - / * 
# power of **
# floor division // 10//3 = 3
# modulo % - 10%3 = 1 

length = int(input("enter the length of the rectangle: ")) 
width = int(input("enter the width of rectangle: "))

perimeter = 2 * (length + width)

print("perimeter: ", perimeter)

"""
dfgsfdgvdvsd - docstring 
"""