def count(sequence, item):
  sum = 0
  for n in sequence:
    if n == item:
      sum += 1
  return sum

def test_count_int():
  assert count([1, 2, 3, 4, 4, 5, 4], 4) == 3
  assert count([1, 2, 4, 0, -2, -4, -4], 0) == 1
  assert count([], 2) == 0

def test_count_str():
    assert count(["apple", "apple", "banana", "pear"], "apple") == 2
    assert count(["pear", "apple", "orange", "banana"], "pear") == 1
    assert count([], "banana") == 0

#2 
def fact(x):
    if x == 0:
        return 1
    return x * fact(x - 1)

def test_fact():
    assert fact(0) == 1
    assert fact(1) == 1
    assert fact(5) == 120
    assert fact(10) == 3628800

#3
def list_of_squares(n):
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    return d

def test_list_of_squares():
    assert list_of_squares(1) == {1: 1}
    assert list_of_squares(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    assert list_of_squares(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

#4
def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels

def test_vowels():
    assert vowels("xyz") == 0
    assert vowels("aeiou") == 5
    assert vowels("AEIOU") == 5
    assert vowels("Hello World") == 3