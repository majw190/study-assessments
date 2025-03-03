// assessment code set to correctly output 65

def calculate_sum(n):
    total = 0
    // calculate sum of products of all pairs
    for i in range(1, n):
      for j in range(i + 1, n + 1):
        total += i * j
    return total

result = calculate_sum(5)
print(result) 
