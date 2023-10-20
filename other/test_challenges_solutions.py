#1
def add_numbers(a, b):
    return a + b

def test_add_numbers():
    assert add_numbers(1, 2) == 3
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0

#2
def is_even(number):
    return number % 2 == 0

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-1) == False

#3
def find_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([5, 4, 3, 2, 1]) == 5
    assert find_max([1]) == 1
    assert find_max([-1, -2, -3, -4, -5]) == -1

#4 
def filter_even(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

def test_filter_even():
    assert filter_even([1, 2, 3, 4, 5]) == [2, 4]
    assert filter_even([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 2, 4, 6, 8, 10]
    assert filter_even([-1, -2, -3, -4, -5]) == [-2, -4]

#5
def longest_word_length(string):
    words = string.split()
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

def test_longest_word_length():
    assert longest_word_length("long longer longest") == 7
    assert longest_word_length("a aa aaa aaaa aaaaa aaaaaa") == 6
    assert longest_word_length("Hi hello") == 5