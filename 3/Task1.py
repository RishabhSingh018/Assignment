def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial((n-1))
number=int(input('Enter a Number: '))
result=factorial(number)
print(f"Factorial of 5 is: {result}")