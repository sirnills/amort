import sys


def monthly_payment(rate, term, principle):
    rate = float(rate)/100/12
    principle = int(principle)
    term = int(term)
    payment = principle * ((rate * (1 + rate) ** term) / (((1 + rate) ** term) - 1))
    return payment


def amort_start(rate=4.5, principle=312750, term=360):
    if rate is None:
        rate = input("What is the interest rate for the loan: ")

    if principle is None:
        principle = input("What is the amount financed: ")

    if term is None:
        term = input("what is the number of terms: ")
    monthly = (round(float((monthly_payment(rate, term, principle))), 2))
    print ""
    print "***********************************************************************"
    print "Here is your monthly payment: ", monthly
    print "Here is the total amount paid over [test] the life of the loan: ", (monthly * term)
    print ""
    print "-----------------------------------------------------------------------"

    data = []
    for i in range(term):
        interest_payment = principle * (rate / 100 / 12)
        principle_payment = monthly - interest_payment
        principle = principle - principle_payment

        d = {}
        d['term'] = i
        d['principle'] = round(principle, 2)
        d['principle_payment'] = round(principle_payment, 2)
        d['interest_payment'] = round(interest_payment, 2)
        i += 1

        data.append(d)

    return rate, principle, term, monthly, data


def additional_data(args):
    decision = raw_input('Would like to know data for any specific term payment?yes, no, or exit ')
    while decision in ("yes", "y", "no", "n", "exit", "e"):
        if decision == "yes" or decision == "y":
            value_month = int(input("Which term month payment would you like to see? "))
            print"The term month you requested: ", str(value_month)
            print"Remaining Principle: ", data[value_month - 1][1]
            print"Amount paid on principle: ", data[value_month - 1][2]
            print"Amount paid in interest: ", data[value_month - 1][3]
        elif decision == "no" or decision == "n":
            print("Okay! Fine!")
            sys.exit()
        elif decision == "exit" or decision == "e":
            print("Good-Bye!!!")
            sys.exit()
            return


    def wack_bang():
        con = raw_input('Enter(1) to restart program, Enter(2) to view data from another month, Enter(3) to exit? ')
        if con == "1":
            amort_start()
        elif con == "2":
            additional_data(data)
        elif con == "3":
            print("Okay! Fine!")
        else:
            wack_bang()


if __name__ == '__main__':
    # r, p, t, m, d = amort_start(4.5, 312750)
    while True:
        con = raw_input('Enter(1) to Start program or Enter(2) to exit? ')
        if con == "1":
            amort_start()
            additional_data()
        elif con == "2":
            sys.exit()






