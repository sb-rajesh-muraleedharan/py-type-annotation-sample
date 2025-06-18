# py-type-annotation-sample

A collection of Python code samples demonstrating the use of type annotations, including `Any`, `Optional`, `Union`, `TypedDict`, and lambda functions. This project is intended for educational purposes and to illustrate best practices for type hinting in Python 3.12+.

## Contents

- `main.py`: Entry point for the project.
- `any-sample.py`: Demonstrates the use of `Any` from the `typing` module.
- `optional-sample.py`: Shows how to use `Optional` for nullable types.
- `union-sample.py`: Explains the use of `Union` for multiple possible types.
- `typed_dict_sample.py`: Example of using `TypedDict` for type-safe dictionaries.
- `lambda-sample.py`: Examples of lambda functions and their use with `map`.

## Requirements
- Python 3.12 or higher

## Setup
1. (Optional) Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage
You can run each sample file directly. For example:

```bash
python any-sample.py
python optional-sample.py
python union-sample.py
python typed_dict_sample.py
python lambda-sample.py
```

## File Descriptions

### any-sample.py
Demonstrates the use of `Any` to allow a function to accept and return values of any type. Includes error handling for empty lists.

### optional-sample.py
Shows how to use `Optional` to indicate that a function argument can be `None` or a specific type.

### union-sample.py
Explains the use of `Union` to allow a function to accept multiple types and handle them accordingly.

### typed_dict_sample.py
Provides an example of using `TypedDict` to define dictionaries with specific, type-checked fields.

### lambda-sample.py
Contains examples of lambda functions, including squaring a number and using `map` with a lambda.

## License
This project is for educational purposes.