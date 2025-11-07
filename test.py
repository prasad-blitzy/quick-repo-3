from typing import Union
from numbers import Number
import math

"""Module for robust numeric addition operations."""


def add_numbers(a: Union[int, float, Number], b: Union[int, float, Number]) -> Union[int, float]:
    """Add two numbers together with comprehensive input validation.
    
    This function performs addition of two numeric values with robust error handling
    and validation to ensure reliable operation in production environments. It validates
    input types, checks for special numeric values, and handles edge cases appropriately.
    
    Parameters
    ----------
    a : Union[int, float, Number]
        The first numeric value to add. Must be a valid number (int, float, or any
        numeric type implementing the Number abstract base class).
    b : Union[int, float, Number]
        The second numeric value to add. Must be a valid number (int, float, or any
        numeric type implementing the Number abstract base class).
        
    Returns
    -------
    Union[int, float]
        The sum of the two input numbers. Returns an integer if both inputs are integers,
        otherwise returns a float.
        
    Raises
    ------
    TypeError
        If either parameter is None or not a numeric type.
    ValueError
        If either parameter is NaN (Not a Number) or infinity, or if the addition
        result exceeds numeric bounds (produces infinity).
        
    Examples
    --------
    >>> add_numbers(5, 3)
    8
    >>> add_numbers(2.5, 3.7)
    6.2
    >>> add_numbers(-10, 15)
    5
    >>> add_numbers(0, 0)
    0
    """
    # Check for None values
    if a is None or b is None:
        param_name = 'a' if a is None else 'b'
        raise TypeError(f"Parameter '{param_name}' cannot be None. Both parameters must be numeric values.")
    
    # Validate that inputs are numeric types
    if not isinstance(a, Number):
        raise TypeError(f"Parameter 'a' must be a number, got type '{type(a).__name__}'")
    if not isinstance(b, Number):
        raise TypeError(f"Parameter 'b' must be a number, got type '{type(b).__name__}'")
    
    # Check for NaN (Not a Number) values
    try:
        if math.isnan(float(a)):
            raise ValueError("Parameter 'a' is NaN (Not a Number). NaN values are not allowed.")
    except (ValueError, OverflowError):
        # If conversion to float fails or value is too large, continue with other checks
        pass
    
    try:
        if math.isnan(float(b)):
            raise ValueError("Parameter 'b' is NaN (Not a Number). NaN values are not allowed.")
    except (ValueError, OverflowError):
        pass
    
    # Check for infinity values
    try:
        if math.isinf(float(a)):
            raise ValueError("Parameter 'a' is infinity. Infinite values are not allowed.")
    except (ValueError, OverflowError):
        pass
    
    try:
        if math.isinf(float(b)):
            raise ValueError("Parameter 'b' is infinity. Infinite values are not allowed.")
    except (ValueError, OverflowError):
        pass
    
    # Perform the addition operation
    result = a + b
    
    # Check if the result is infinite (overflow condition)
    try:
        if math.isinf(float(result)):
            raise ValueError("Addition result exceeds numeric bounds and produces infinity.")
    except (ValueError, OverflowError):
        pass
    
    # Return the result
    return result


if __name__ == "__main__":
    # Demonstration of valid additions
    print("Valid integer addition:")
    print(f"add_numbers(5, 3) = {add_numbers(5, 3)}")
    
    print("\nValid float addition:")
    print(f"add_numbers(2.5, 3.7) = {add_numbers(2.5, 3.7)}")
    
    print("\nMixed type addition:")
    print(f"add_numbers(10, 5.5) = {add_numbers(10, 5.5)}")
    
    print("\nNegative number addition:")
    print(f"add_numbers(-10, 15) = {add_numbers(-10, 15)}")
    
    print("\nZero addition:")
    print(f"add_numbers(0, 0) = {add_numbers(0, 0)}")
    
    # Demonstration of error handling
    print("\nError handling examples:")
    
    try:
        add_numbers(None, 5)
    except TypeError as e:
        print(f"TypeError caught: {e}")
    
    try:
        add_numbers("10", 5)
    except TypeError as e:
        print(f"TypeError caught: {e}")
    
    try:
        add_numbers(float('nan'), 5)
    except ValueError as e:
        print(f"ValueError caught: {e}")
    
    try:
        add_numbers(float('inf'), 5)
    except ValueError as e:
        print(f"ValueError caught: {e}")
