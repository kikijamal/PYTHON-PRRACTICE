# Function to find sum of digits of a number
def sum_of_digits(num):
    """
    This function calculates the sum of all digits in a number.
    """
    if num < 0:
        num = -num  # Handle negative numbers
    total = 0
    while num > 0:
        digit = num % 10  # Get last digit
        total += digit    # Add it to sum
        num //= 10        # Remove last digit
    return total

# Example usage
if __name__ == "__main__":
    number = 1234
    print("Sum of digits:", sum_of_digits(number))  # Output: 10
