salary = int(input("Enter your salary:"))
age = int(input("Enter your age:"))
if salary >= 20000 and age <= 25:
    loan_amt = int(input("enter the loan_amt"))
    if loan_amt < 50000:
        print("You are eligible for loan")
    else:
        print("Maximum loan amount is 50,000")

else:
    print("You are not eligible for loan")
