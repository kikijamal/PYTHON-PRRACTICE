# Function to sum all elements in a list
def sum_list(numbers):
    """
    This function takes a list of numbers and returns the total sum.
    """
    total = 0  # Initialize sum
    for num in numbers:
        total += num  # Add each number to total
    return total

# Example usage
if __name__ == "__main__":
    sample_list = [10, 20, 30, 40]
    print("Sum of list:", sum_list(sample_list))  # Output: 100
