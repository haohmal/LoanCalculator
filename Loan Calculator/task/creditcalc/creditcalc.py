import math
import argparse
import sys

arg_parser = argparse.ArgumentParser(description="This program calculates loans.")
arg_parser.add_argument("--type", choices=["annuity", "diff"], help="Choices are annuity or diff")
arg_parser.add_argument("--payment", help="The monthly payment amount.")
arg_parser.add_argument("--principal")
arg_parser.add_argument("--periods", help="Denotes the number of months needed to repay the loan.")
arg_parser.add_argument("--interest")

args = arg_parser.parse_args()

if args.type != "diff" and args.type != "annuity":
    print("Incorrect parameters")
    sys.exit(-1)

if args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    sys.exit(-1)

#if len(args) != 5:
#    print("Incorrect parameters")
#    sys.exit(-1)

annuity = 0
principal = 0
nominal_interest = 0
interest = 0
number = 0
num_params = 0

if args.principal is not None:
    principal = float(args.principal)
    if principal <= 0:
        print("Incorrect parameters")
        sys.exit(-1)
    num_params += 1
else:
    mode = 'p'

if args.periods is not None:
    number = int(args.periods)
    if number <= 0:
        print("Incorrect parameters")
        sys.exit(-1)
    num_params += 1
else:
    mode = 'n'

if args.payment is not None:
    annuity = float(args.payment)
    if annuity <= 0:
        print("Incorrect parameters")
        sys.exit(-1)
    num_params += 1
else:
    mode = 'a'

if args.interest is not None:
    interest = float(args.interest)
    if interest <= 0:
        print("Incorrect parameters")
        sys.exit(-1)
    num_params += 1
else:
    print("Incorrect parameters")
    sys.exit(-1)

if args.type == "diff":
    mode = 'd'

if num_params != 3:
    print("Incorrect parameters")
    sys.exit(-1)

def get_diffetentiated_payment(principal, nominal_interest, number, month):
    part1 = principal * ((month - 1) /number)
    return math.ceil(principal / number + nominal_interest * (principal - part1))

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

if mode == 'd':
    total_payment = 0
    for month in range(number):
        month += 1
        payment = get_diffetentiated_payment(principal, get_nominal_interest(interest), number, month)
        total_payment += payment
        print("Month {0}: payment is {1}".format(month, payment))
    print()
    print("Overpayment = {}".format(total_payment - principal))
elif mode == 'p':
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
    if months > 0:
        print("It will take {0} years and {1} months to repay this loan!".format(years, months))
    else:
        print("It will take {0} years to repay this loan!".format(years))
    total_payment = number * annuity
    print("Overpayment = {}".format(total_payment - principal))