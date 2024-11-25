def factorial(n: int) -> int:
    # base case
    if n in [0, 1]:
        return n
    elif n < 0:
        return 0
    else:
        # recursive implementation
        return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    # base case
    if n in [0, 1]:
        return n
    elif n < 0:
        return 0
    else:
        # recursive implementation
        return fibonacci(n - 1) + fibonacci(n - 2)
