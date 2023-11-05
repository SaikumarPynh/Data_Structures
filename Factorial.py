def Factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * Factorial(n-1)
    
n = int(input("enter the size of the factorial:"))
result = Factorial(n)
print("Factorial of a number is:",result)
