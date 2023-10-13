# iteration is another word for loops, repeating blocks of code over and over. 
# saves time without having to write our code multiple times. 

# 2 types of loops:
# while loops
# for loops


# while loops
# a while loop will continuously execute code whilst a condition is true.
# or when another condition is met.
# if a condition is never true the while loop with never start.

#print("1")
#print("2")
#print("3")....

#x = 0

#while x < 100:
#    print(x)
#    x += 1

# break

#i = 1

#while i < 6:
 #   if i == 3:
#        break
#    print(i)
#    i += 1 

# continue 

#j = 0

#while j < 6:
#    j += 1
#    if j == 3:
#        continue
#    print(j)

#k = 1#

#while k < 6:
#    print(k)
#    k += 1
#else:
#    print("k is no longer less than 6")

# while true loop

#while True:
#    name = input("enter your name: ")
#    if name == "quit":
#        break
#    else:
#        print(f"hello {name}")

# for loops
# a for loop will iterate over any iterable collection: lists/strings/dictionaries
# useful for when we want to use data from a collection
# Do things to individual items in a collection

# iterating through lists 

#my_fruits = ["apple", "orange", "pear"]

#for fruits in my_fruits:
 #   print(fruits)

#numbers = [1, 2, 3, 4]

#for item in numbers:
#    print(item)

#l = 0

#while l < len(numbers):
#    print(numbers[l])
#    l += 1   

# range 

for a in range(5):
    print(a)

for a in range(1,5):
    print(a)

for a in range(1, 10, 2):
    print(a) # 1-9 in steps of 2.

# stings

for letter in "hello":
    print(letter)

for word in "hello world".split():
    print(word)

# list comprehension

result = [x**2 for x in range(5)]
print(result)

results = []

for x in range(5):
    results.append(x**2)
    print(results)

# dictionaries

for i in {"drink": "wine"}:
    print(i)

for i in {"food": "jam"}.values():
    print(i)

for i in {"shape": "square"}.items():
    print(i)

# break and continue

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    print(i)
    if i == 5:
        break

# nested loops

for i in range(1,3):
    for j in range(1,4):
        print(i, "x", j, "=", i*j)

# write a while loop that asks for the names of 5 people.
# for each person print out their name, followed by some text
# "is awesome".
# counter + while loop, an input, a print, a +=1.



