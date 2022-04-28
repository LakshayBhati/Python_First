# WAP to make a simple Calculator
print("Select one Operation you want to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter your choice: ")
    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter the First Number: "))
        b = float(input("Enter the Second Number: "))
        if choice == '1':
            sum = a + b
            print("The Addition of the two numbers is: ",sum)
        elif choice =='2':
            sub = a - b
            print("The Subtraction of the two numbers is: ",sub)
        elif choice == '3':
            mul = a * b
            print("The Multiplication of the two numbers is: ",mul)
        elif choice == '4':
            div = a / b
            print("THe Division of the two numbers is: ",div)

        con = input("Do you want to continue [Y/N]: ")
        if con == ('N' or 'n'):
            break
    else:
        print("You entered the wrong choice!")

