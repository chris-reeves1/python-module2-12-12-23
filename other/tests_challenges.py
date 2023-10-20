#1
def add_numbers(a, b):
    return a + b

#2
def is_even(number):
    return number % 2 == 0

#3
def find_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

#4 
def filter_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

#5
def longest_word_length(string):
    words = string.split()
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length