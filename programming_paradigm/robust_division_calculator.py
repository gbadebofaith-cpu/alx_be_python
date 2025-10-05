def safe_divide(numerator, denominator):
    """Performs division safely, handling errors like zero division and non-numeric input."""
    try:
        # Try converting inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Try performing the division
        result = num / denom
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
