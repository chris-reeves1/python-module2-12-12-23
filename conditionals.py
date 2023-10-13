# if, elif, else statements. (flow control) 
# conditional statements are used to accomodate different paths out code can follow.

my_bool = False

if my_bool:
    print("my bool is true")
else:
    print("my bool is false") 

# nested if statements

#if some_condition:
#    if some_other_condition:
#        .....
#    else:
#        .....
#else:
#    ....

#conditionals:

# equals to: == 
# not equal to: !=
# less than: <
# more than: >
# less than or equals to: <=  -  >=    

# examples

#money = 10

#if money > 11:
#    print("i have some money") 
#else:
#    print("i dont have much money")

# elif - else if
# we dont always want to check if every if statement equates to true 
# mostly only one statement will be true 
# elif makes our code more efficiant
# will only run if no other conditional was evaluated as true

#temp = 10

#if temp >= 30:
#    print("its very hot today")
#elif temp > 25:
#    print("its pretty hot")
#elif temp > 20:
#    print("its ok")
#elif temp > 15:
#    print("could be better")
#elif temp == 0:
#    print("its freezing")
#else:
#    print("generally bad")

# exercise:

# ask for an input from a user for a grade/mark
# if the mark is greater than 85 print 'distiction'.
# if the mark is between 65 and 85 print 'pass'
# anything else print 'fail'
# if elif else - if if else

#x = int(input("enter a grade: "))

#if x >= 85:
#    print("distinction")
#elif x >= 65:
#    print("pass")
#else:
#    print("fail")

# Multiple compareters - with multiple ocnditions using and/or

#deposit = 10
#password = "password1"

#if 0 < deposit <= 100 and password == "password":
#    print(f"thank you for your deposit of £{deposit}")
#else:
#    print("failed to deposit")

#if not (0 < deposit <= 100) or password != "password":
#    print("failed to deposit")
#else:
#    print("thank you for the deposit")

# in and not in

#name = "root123"

#if name in ("root", "admin", "user"):
#    print("invalid username")
#else:
#    print("accepted")

#if name not in ("root", "admin"):
    #print("accepted")
#else:
    #print("invalid username")

# challenge
# weight converter app: convert a user inputted weight(float),
# and user to select either Kgs or Lbs.
# write an if statement that checks if the unit is Kgs or Lbs
# and print the converted value. If Kgs print out in Lbs. 
# else: to handle the other conversion. 
# Error handling for upper/lower case input.
    

