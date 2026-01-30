def print_factor(x):
    """Print all factors of the given number x"""
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    print(f"Factors of {x}: {factors}")
    print(f"Total factors: {len(factors)}")
    return factors

print("Exercise 2: Function to print factors")
print_factor(20)  # Test with a smaller number

print("\n" + "="*50 + "\n")