from typing import Union

# This function demonstrates the use of Union type annotation.
# It processes input data that can be either an int or a str.
def process_data(data: Union[int, str]) -> str:
    # Check if data is an integer and process accordingly
    if isinstance(data, int):
        return f"Processed integer: {data}"
    # Check if data is a string and process accordingly
    elif isinstance(data, str):
        return f"Processed string: {data}"
    else:
        # Raise an error if data is neither int nor str
        raise ValueError("Unsupported data type")

def process_item(item: int | str):
    #Pipe Operator (|): Introduced in Python 3.10 (as described in PEP 604), 
    #the pipe operator provides a more concise way to represent union types.
    print(f"Processing item: {item}")    

# Example usage
if __name__ == "__main__":  
    # Call with an integer
    print(process_data(42))          # Processed integer: 42
    # Call with a string
    print(process_data("Hello"))     # Processed string: Hello
    # The following line, if uncommented, will raise ValueError because 3.14 is not int or str
    # print(process_data(3.14))      # Uncommenting this line will raise ValueError
    process_item(100)                # Processing item: 100
    #process_item(100.2)      # Invalid type
