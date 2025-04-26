# Function to calculate factorial using a loop
def factorial_loop(n):
    """
    This function calculates the factorial of a number using a for loop.
    """
    if n < 0:
        return "Invalid! Factorial not defined for negative numbers."

    result = 1  # Start from 1 because factorial starts from 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by current number
    return result

# Example usage
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is", factorial_loop(num))  # Output: 120
