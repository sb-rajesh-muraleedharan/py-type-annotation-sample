from typing import TypedDict, Union

# Define a TypedDict for a Movie with specific types for each field
class Movie(TypedDict):
    name: str  # Movie name must be a string
    year: Union[int]  # Movie year must be an integer

if __name__ == "__main__":  
    # Example usage: This will raise a type error because 'year' should be an int, not a string
    movie = Movie(name="Inception", year="5555")
    print(movie)
