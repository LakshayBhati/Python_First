# WAP to find a factorial of a number
num = int(input("Enter a number to find its Factorial: "))

factorial = 1

if (num<0):
    print("Factorial of Negative numbers do not exist.")
elif (num==0):
    print("Factorial of 0 is 1!")
else:
    for i in range(1, num+1):
        factorial*= i
print("The factorial of the number ",num," is: ",factorial)