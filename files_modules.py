# modules

# module are just files that we use to extend our functionality.
# we can import existing modules or make our own.
# many modules are built-in and do not reuire any set up. 
# some need to be installed - with pip.  

#import math # importing the entire module.

#number = 10

#answer = math.sqrt(number) # syntax for referencing an object from a module. 

#print(answer)

#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)

#for i in range(5):
#    print(random_pi())

# Just with the desired objects = save memory + increase performance

#from math import pi, ceil, floor
#from random import randint

#def random_pi():
#    return floor(randint(1,10) * pi)

#for i in range(1,10):
#    print(random_pi())

# exerice: create 2 files, one called dice.py - write a function 
# that will generate a random number between 1 and 6. In the second file 
# use the dice module to simulate throwing 2 dice and print it's value.   

# files
# read, write, and edit files
# most file types will work, some will need to import modules.
# lets focus on .txt files.

# eg:

# file = open("filename.txt", "mode") # mode can be r (read-only), 
# w (write), r+ (read and write) a (append). 

# file.close() # Must remeber to close the file after use. most recently opened file will close. 

# to read:

#file = open("lines.txt", "r")

#lines = file.readlines()

#print(lines)

#file.close()

# writing files

#file = open("line1.txt", "w")

#for n in range(1, 11):
#    newline = "this is line" +  " " + str(n) + "\n"
#    file.write(newline)

#file.close()


#file = open("line1.txt", "r")

#outfile = ""

#for line in range(1, 10):
#    if line % 2 == 0: # even numbers
#        outfile += file.readline()
#    else:
#        file.readline()

#file = open("line1.txt", "w")

#file.write(outfile)

#file.close()

# exercise - open a new text file called teams.txt, add the names of 5 sports teams.
# read and display the names of the 1st and 4th team .strip()
# edit the file so that the top line is replaced with "this is a new line"
# print out the edited file, line by line. 














