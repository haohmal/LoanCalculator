import math

annuity = 0
principal = 0
nominal_interest = 0
interest = 0
number = 0


def get_loan_principal(annuity, nominal_interest, number):
    part1 = nominal_interest * math.pow(1 + nominal_interest, number)
    part2 = math.pow(1 + nominal_interest, number) - 1
    return annuity / (part1 / part2)


def get_number_of_payments(annuity, nominal_interest, principal):
    return math.log((annuity / (annuity - nominal_interest * principal)), 1 + nominal_interest)


def get_nominal_interest(interest):
    return interest / 100 / 12


def get_annuity(principal, nominal_interest, number):
    return math.ceil(principal * nominal_interest * math.pow(1 + nominal_interest, number) / (
                math.pow(1 + nominal_interest, number) - 1))


print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
mode = input()

if mode != 'p':
    print("Enter the loan principal:")
    principal = int(input())

if mode != 'a':
    print("Enter the annuity payment:")
    annuity = float(input())

if mode != 'n':
    print("Enter the number of periods:")
    number = float(input())

print("Enter the loan interest:")
interest = float(input())

if mode == 'p':
    #print("Your loan principal = 800000!")
    principal = get_loan_principal(annuity, get_nominal_interest(interest), number)
    print("Your loan principal = {}!".format(principal))
elif mode == 'a':
    annuity = get_annuity(principal, get_nominal_interest(interest), number)
    print("Your monthly payment = {}!".format(annuity))
else:
    number = math.ceil(get_number_of_payments(annuity, get_nominal_interest(interest), principal))
    years = number // 12
    months = number % 12
    print("It will take {0} years and {1} months to repay this loan!".format(years, months))
