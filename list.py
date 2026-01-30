# COMP7940 Exercise 3: List Iteration
# Simple and clear implementation

l = [52633, 8137, 1024, 999]

# Function from Exercise 2
def print_factor(x):
    """Print all factors of x"""
    factors = [i for i in range(1, x + 1) if x % i == 0]
    print(f"Factors of {x}: {factors}")
    return factors

# Apply to list (Exercise 3)
print("Applying function to list:", l)
for num in l:
    print_factor(num)