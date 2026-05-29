# Function to calculate factorial
def factorial(n):
    fact = 1
    
    # Loop to calculate factorial
    for i in range(1, n + 1):
        fact = fact * i
    
    return fact

# Calling the function with a sample number
num = 5
result = factorial(num)

# Printing the output
print("Factorial of", num, "is:", result)