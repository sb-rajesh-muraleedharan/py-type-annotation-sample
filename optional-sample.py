from typing import Optional

# This function demonstrates the use of Optional type annotation.
# It processes a string if provided, otherwise returns a default message.
def process_data(data: Optional[str]) -> str:
    # Check if data is None and return a default message if so
    if data is None:
        return "No data provided"
    else:
        # Return a message indicating the data is being processed
        return f"Processing data: {data}"

def say_hello(name: str | None = None) -> str:
    """
    Returns a greeting message. If name is None, returns a default greeting.
    
    Args:
        name (Optional[str]): The name to greet. Defaults to None.
        
    Returns:
        str: A greeting message.
    """
    if name is None:
        return "Hello, stranger!"
    else:
        return f"Hello, {name}!"

# Example usage
if __name__ == "__main__":  
    # Call with None to show the default message
    print(process_data(None))  # Output: No data provided
    # Call with a string to show the processing message
    print(process_data("Sample data"))  # Output: Processing data: Sample data
    # Call the say_hello function with a name
    print(say_hello("Alice"))  # Output: Hello, Alice!
    # Call the say_hello function without a name
    print(say_hello())  # Output: Hello, stranger!
    # Call the say_hello function with an empty string
    print(say_hello(""))  # Output: Hello, !