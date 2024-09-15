def recursive_factorial(x):
    if x == 1:
        return 1
    else:
        return x * recursive_factorial(x-1)

def iterative_factorial(x):
    result = 1
    for i in range(1, x+1):
        result *= i
    return result
