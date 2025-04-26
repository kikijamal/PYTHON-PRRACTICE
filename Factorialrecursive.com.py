# Function to calculate factorial using recursion
def factorial_recursive(n):
    """
    This function calculates the factorial of a number using recursion.
    """
    if n < 0:
        return "Invalid! Factorial not defined for negative numbers."
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial_recursive(n - 1)  # Recursive case

# Example usage
if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} (recursive) is", factorial_recursive(num))  # Output: 120
