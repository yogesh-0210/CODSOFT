print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")
while True:
    operations=input("Enter the operations to Perform:")
    
    if operations in("1","2","3","4"):
        try:
            a=int(input("Enter Num1:"))
            b=int(input("Enter Num2:"))
        except ValueError:
            print("Invalid input,Please Enter the Valid Number")

            continue
    
        if operations == "1":
            print("The Sum of Two Numbers =" +str(int(a)+int(b)))
        elif operations =="2":
            print("The Difference of Two Numbers =" +str(int(a)-int(b)))
        elif operations =="3":
            print("The Product of Two Numbers =" +str(int(a)*int(b)))
        elif operations == "4":
            print("The Dividion of Two numbers =" +str(int(a)/int(b)))
        else:
            print("Invalid input. Please choose a valid operation.")
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break
    else:
        print("Invalid input. Please choose a valid operation.")
