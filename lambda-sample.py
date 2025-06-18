# This function demonstrates a simple lambda that squares a number
# and prints the result for the value 10.
def lambda_function(x):
    # Define a lambda function that squares its input
    square = lambda x: x * x
    print(square(10))

# This function demonstrates using lambda with map to square a list of numbers
def map_function(nums):    
    # Use map with a lambda to square each number in the list
    squared_nums = list(map(lambda x: x * x, nums))
    print(squared_nums)

# Run the functions if this script is executed directly
if __name__ == "__main__":
    lambda_function(10)
    map_function([1, 2, 3, 4, 5])