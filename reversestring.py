# Function to reverse a string without using slicing or built-in functions
def reverse_string(s):
    """
    This function reverses a string manually without using [::-1] or reversed().
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # Add each character to the front
    return reversed_str

# Example usage
if __name__ == "__main__":
    original = "Python"
    print("Reversed string:", reverse_string(original))  # Output: nohtyP
