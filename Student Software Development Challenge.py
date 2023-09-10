# Student Software Development Challenge

# Reverse an input string (example: "Hello World" => "dlroW olleH")
def reverse_string(str):
    reversed_string = []
    for i in range(len(str) - 1, 0 - 1, -1):
        reversed_string.append(str[i])
    return("".join(reversed_string))

print(reverse_string("hey buddy"))


# Find the largest integer out of three inputs
# (This one uses a built in function that felt like cheating for this assignment)
def find_largest_integer_builtin(int1, int2, int3):
    return max(int1, int2, int3)

# (This one is my own work)
def find_largest_integer(int1, int2, int3):
    integers = [int1, int2, int3]
    current_max = int1
    for i in integers:
        if i > current_max:
            current_max = i
    return(current_max)

print(find_largest_integer(1, 2, 3))


# Calculate the factorial of n
def calculate_factorial(n):
    if n == 1:
        return n
    else:
        return n * calculate_factorial(n-1)
    
def calculate_factorial_advanced(n):
    result = lambda num : num if num == 1 else num * calculate_factorial_advanced(num-1)
    return result(n)

print(calculate_factorial_advanced(3))


# Calculate the 'n'th entry of the Fibonacci sequence
def calculate_fibonacci(n):
    value = 1
    previous_value = 0
    for i in range(0, n-1, 1):
        newvalue = value + previous_value
        previous_value = value
        value = newvalue
    return(value)

print(calculate_fibonacci(5))