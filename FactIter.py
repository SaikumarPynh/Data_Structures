def Factorial(n):
    result = 1
    if n == 1 or n == 0:
        return result
    else:
        for i in range(1,n+1):
            result = result * i
        return result

n = int(input("enter the size of the factorial:"))
result = Factorial(n)
print("Factorial of a number is:",result)

