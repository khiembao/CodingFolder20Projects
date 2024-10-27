def main():
    print("this is a monthly payment calculator ")
    print("")

    principal = float(input("input the loan amount: "))
    apr = float(input("input the annual interest rate: "))
    years = int(input("input the amount of year: "))

    monthly_interest_rate = apr/1200
    amount_of_month = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 -(1 + monthly_interest_rate) ** (-amount_of_month))

    print("The monthly payment from this loan is: %.2f" % monthly_payment)

main()    