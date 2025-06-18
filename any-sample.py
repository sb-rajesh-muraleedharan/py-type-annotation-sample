from typing import Any

# This function demonstrates the use of the 'Any' type from the typing module.
# It returns a random element from a list of any type.
def any_sample(data: list[Any]) -> Any:
    """
    Returns a random element from the provided list.

    Args:
        data (list[Any]): The list from which to select a random element.

    Returns:
        Any: A random element from the list.
    """
    import random
    # Check if the input list is empty and raise an error if so
    if not data:
        raise ValueError("The input list cannot be empty.")
    # Return a random element from the list
    return random.choice(data)

# Example usage:
if __name__ == "__main__":
    # Define a sample list of integers
    sample_list = [1, 2, 3, 4, 5]
    # Print a random element from the sample list
    print(any_sample(sample_list))  # Outputs a random element from the list
    # print(any_sample([]))  # Raises ValueError