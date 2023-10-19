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
