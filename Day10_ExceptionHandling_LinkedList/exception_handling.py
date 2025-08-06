def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except ValueError:
        return "Error: Invalid input"
    else:
        return f"Result = {result}"
    finally:
        print("Division attempt completed.")

try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    print(safe_divide(x, y))
except ValueError:
    print("Please enter valid integers only.")
