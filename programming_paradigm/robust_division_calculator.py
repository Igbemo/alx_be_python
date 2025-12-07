def safe_divide(numerator, denominator):
    """
    Performs division with robust error handling.
    
    Handles:
    - Division by zero
    - Non-numeric inputs
    Returns either the result as a string or an error message.
    """
    try:
        # Convert inputs to float
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        try:
            result = num / den
            return f"The result of the division is {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
