# different ways of storing data
# lists - ordered, mutable (rwd), collection of values [a ,b ,c ...] 
# dictionaries unordered, mutable collection of key-pair values {"key": "value"}
# sets - unordered, mutable, collection of unique values {value1, value2}
# tuples - ordered, immutable, colelction of values (value1, value 2...)

# lists are stored in a variable = []

#colours = ["blue", "red", "green", "yellow"]

#print(colours)

# referencing elements in a list is by their index position
# starts at [0] and also [-1] 

#print(colours[0])
#print(colours[3])
#print(colours[-4])

# slicing - create a sub-list up to but not including the 2nd number in the range

#print(colours[0:2])
#print(colours[1:]) # no 2nd number slices till the end of the list

# altering lists - use index position, need a value, delete with del

#food = ["bread", "cheese", "pasta", "apple"]

#print(food)
#food[0] = "rice" 
#print(food)
#del food[1]
#print(food)

# Checking if item is in a list

#print("pasta" in food)
#print("orange" in food)

# nested list

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# multiple data types

#my_list = ["red", 5, ["green", "apple"], 10.5]

#print(my_list)
#print(my_list[2][1])
#print(my_list[0])

# list methods

# append 

#my_fruits = ["apple", "orange", "kiwi"]


#my_fruits.append("pear")
#print(my_fruits)

# remove

#my_fruits.remove("apple")
#print(my_fruits)

# insert 

#my_fruits.insert(0, "mango")
#my_fruits.insert(0, "melon")
#print(my_fruits)


# extend - with a list

#my_fruits.extend(["grapes", "cherry"])
#print(my_fruits)

# finding index position

#print(my_fruits.index("mango"))

# reversing

#my_fruits.reverse()
#print(my_fruits)

# sorting

#my_fruits.sort()
#print(my_fruits)
#my_fruits.sort(key=len)
#print(my_fruits)

# join

#x = ", ".join(my_fruits)
#print(x)
#print(type(x))

# Dictionaries {} key:value pairs
# similar to a list, but not indexing
# keys need to be unique, values dont

drinks = {"fizzy": "sprite", "still": "water", "juice": "orange", "alcohlic": "wine"}

print(drinks)
print(drinks["still"]) # can only query with the key not the value 

# add to my dictionary

drinks["non-alcohlic"] = "water"
print(drinks)

# Overwrite

drinks["non-alcohlic"] = "squash"
print(drinks)

# return all values or keys or both

print(drinks.values())
print(drinks.keys())
print(drinks.items())

print("water" in drinks.values())
print("still" in drinks)

# get method

print(drinks.get("still"))
print(drinks.get("stille"))
print(drinks.get("stillle", "not found"))

# update method - extends dictionary 

drinks.update({"sugery":"cola"})
print(drinks)
drinks.update(very_sugery = "redbull")
print(drinks)

# pop method

print(drinks.pop("non-alcohlic"))
print(drinks.pop("non-alcohlic", "not-found"))
print(drinks)

# exercise:

# Make a dictionary of books, with 3 authors and multiple books per author. 
# Use an input asking for the author Name 
# print back as a string a list of the books by that author.
# use the .join() method

#books_dict = {"author1": ["book1", "book2"], "author2": ["book1", "book2"]}

#y = input("enter author name: ")

#print(", ".join(books_dict[y]))

# tuples
# we cant update a tuple but otherwise is the same as a list
# indicates that we dont want to change the data
# less memory - very slight
# speed - a little bit quicker 
# () instead of [] or nothing at all

shapes = ("square", "circle", "triangle")
shapes1 = "square", "circle", "triangle"

print(type(shapes))
print(type(shapes1))

# sets
# no indexing
# no duplicate values

items = {"apple", "sqaure", "red"}

print(type(items))

