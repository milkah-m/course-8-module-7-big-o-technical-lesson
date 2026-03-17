"""
Algorithms for summing lists with different time complexities.
"""

def sum_list(numbers):
    # TODO: Sum the elements using a single loop.
    # Track the number of iterations and print it.
    total = 0
    count = 0
    for n in numbers:
        total += n
        count += 1
    print(count)
    return total

def sum_list_nested(numbers):
    total = 0
    count = 0
    for i in range(len(numbers)):
        total += numbers[i]
    for j in range(len(numbers)):
        count += 1    	 
    print(f"Total iterations for nested loops: {count}")
    return total

print(sum_list_nested([1,2,3,4,5]))