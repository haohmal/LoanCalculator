print("Enter the loan principal:")
loan = int(input())
print("""What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:""")
mode = input()

if mode == 'm':
    print("Enter the monthly payment:")
    payment = int(input())
    result = loan // payment
    if loan % payment > 0:
        result += 1
    if result == 1:
        print("It will take 1 month to repay the loan")
    else:
        print("It will take " + str(result) + " months to repay the loan")
else:
    print("Enter the number of months:")
    months = int(input())
    last = 0
    if loan % months > 0:
        monthly = (loan // months) + 1
        last = loan - (monthly * (months - 1))
    else:
        monthly = loan // months
    result = "Your monthly payment = " + str(monthly)
    if last > 0:
        result += " and the last payment = " + str(last)
    print(result)
