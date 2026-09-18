
import math

monthly = 0

with open("starttxt.txt", "r", encoding="utf-8") as file:
    intro = file.read()



def press_enter():
    input()



def MSCI_World():
    a_rent = 0.08
    monthly_or_once = input("Do you want to invest monthly or just once? Enter 1 = monthly 2 = one-time.")
    investment = float(input("Enter how much money you want to invest! "))
    years = float(input("How many years do you want to invest? "))
    if monthly_or_once == 1:
        investment = a_rent /12
        years = years * 12
        for month in range(years):
            investment = investment * (1 + investment)
            investment += years
        print("The value in "years" years is:", round(investment, 2))




    

    


def investment_type_request():
    ITR = input("""Which investment method do you want to calculate?

1. MSCI World
2. S&P 500
3. Bank Savings

Please enter your choice:
""")
    if ITR == 1:
        MSCI_World()
    elif ITR == 2:
        SP_500()
    elif ITR == 3:
        Bank_Savings()
    else:
        print("Error: Wrong input!")
        



print(intro)
press_enter()
print("test")

