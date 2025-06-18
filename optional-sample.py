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

# Example usage
if __name__ == "__main__":  
    # Call with None to show the default message
    print(process_data(None))  # Output: No data provided
    # Call with a string to show the processing message
    print(process_data("Sample data"))  # Output: Processing data: Sample data