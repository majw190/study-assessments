// assessment code set to correctly output the total 65

def calculate_sum(n):
    total = 0
    for i in range(1, n):
      for j in range(i, n):
        total += i * j
    return total
  result = calculate_sum(5)
  print(result)
