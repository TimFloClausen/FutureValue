
a_rent = 0

with open("starttxt.txt", "r", encoding="utf-8") as file:
    intro = file.read()


with open("sources.txt", "r", encoding="utf-8") as file:
    sources = file.read()






def press_enter():
    input()


def Q():
    Q = input("Do you want to quit the programm? Y/n ")
    if  Q == "Y":
        print("You quit the programm! Goodbye!" )
        quit
    else:
        print("Decline")



def ETF():
        global a_rent
        monthly_or_once = input("Do you want to invest monthly or just once? Enter 1 = monthly 2 = one-time: ")
        investment = float(input("Enter how much money you want to invest! "))
        years = int(input("How many years do you want to invest? "))
    
        if monthly_or_once == "1":
            monthly_rate = a_rent / 12
            months = years * 12
            total = 0.0
            
    
            for month in range(months):
                total = total * (1 + monthly_rate)
                total += investment

            all_monthly_investment = investment * months

            only_annuel_rent_profit = total - all_monthly_investment

            
            print(f"The value you made only from annual returns in {years} years is: {round(only_annuel_rent_profit, 2)}")
            print(f"The value in {years} years is: {round(total, 2)}")
            Q()
    
        elif monthly_or_once == "2":
            total = investment

    
            for i in range(years):
                total = total * (1 + a_rent)

            only_annuel_rent_profit = total - investment

            


            print(f"The value you made only from annual returns in {years} years is: {round(only_annuel_rent_profit, 2)}") 
            print(f"The value in {years} years is: {round(total, 2)}")
            Q()




def Bank_Savings():
    a_rentb = float(input("Enter your annual rent available in your bank account! "))
    monthly_or_once = input("Do you want to invest monthly or just once? Enter 1 = monthly 2 = one-time: ")
    investment = float(input("Enter how much money you want to invest! "))
    years = int(input("How many years do you want to invest? "))
    


    if monthly_or_once == "1":
        monthly_rate = a_rentb / 12
        months = years * 12
        total = 0.0
        all_monthly_investment = investment * months



        for month in range(months):
            total = total * (1 + monthly_rate)
            total += investment

        only_annuel_rent_profit = total - all_monthly_investment

        print(f"The value you made only from annual returns in {years} years is: {round(only_annuel_rent_profit, 2)}")   
        print(f"The value in {years} years is: {round(total, 2)}")
        Q()

    elif monthly_or_once == "2":
        total = investment

        

        for i in range(years):
            total = total * (1 + a_rentb)

        only_annuel_rent_profit = total - investment

        

        

        print(f"The value you made only from annual returns in {years} years is: {round(only_annuel_rent_profit, 2)}")
        print(f"The value in {years} years is: {round(total, 2)}")
        Q()







def investment_type_request():
    global a_rent
    while True:
        ITR = input("""Which investment method do you want to calculate?

        1. MSCI World
        2. S&P 500
        3. Bank Savings
        4. Dax 40
        5. SMI
        6. Compare Investment Methods
        7. Show Sources

        Please enter your choice:
        """)  
        if ITR == "1":
            a_rent = 0.08 
            ETF()
    
        elif ITR == "2":
            a_rent = 0.10
            ETF()
        elif ITR == "3":
            Bank_Savings()
        elif ITR == "4":
            a_rent = 0.07
            ETF()
        elif ITR == "5":
            a_rent = 0.06
            ETF()
        elif ITR == "6":
            print(sources)
        elif ITR == "7":
            print(sources)
    
        else:
            print("Error: Wrong input!")
            
        

  



print(intro)
press_enter()
print("Let's start with your calculation...")
press_enter()

investment_type_request()



