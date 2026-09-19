
a_rent = 0


with open("starttxt.txt", "r", encoding="utf-8") as file:
    intro = file.read()


with open("sources.txt", "r", encoding="utf-8") as file:
    sources = file.read()






def press_enter():
    input()



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
                
            print(f"The value in {years} years is: {round(total, 2)}")
    
        elif monthly_or_once == "2":
            total = investment
            for i in range(years):
                total = total * (1 + a_rent)
            print(a_rent)  
            print(f"The value in {years} years is: {round(total, 2)}")




def Bank_Savings():
    a_rentb = float(input("Enter your annual rent available in your bank account! "))
    monthly_or_once = input("Do you want to invest monthly or just once? Enter 1 = monthly 2 = one-time: ")
    investment = float(input("Enter how much money you want to invest! "))
    years = int(input("How many years do you want to invest? "))

    if monthly_or_once == "1":
        monthly_rate = a_rentb / 12
        months = years * 12
        total = 0.0

        for month in range(months):
            total = total * (1 + monthly_rate)
            total += investment 
            
        print(f"The value in {years} years is: {round(total, 2)}")

    elif monthly_or_once == "2":
        total = investment
        for i in range(years):
            total = total * (1 + a_rentb)
 
        print(f"The value in {years} years is: {round(total, 2)}")







def investment_type_request():
    global a_rent

    ITR = input("""Which investment method do you want to calculate?

1. MSCI World
2. S&P 500
3. Bank Savings
4. Dax 40
5. Show Sources

Please enter your choice:
""")  
    if ITR == "1":
        a_rent += 0.08 
    
        

    elif ITR == "2":
        SP_500()
        return
    elif ITR == "3":
        Bank_Savings()
    elif ITR == "4":
        Dax()
    elif ITR == "5":
        SMI()
    elif ITR == "Q":
        print(sources)
    else:
        print("Error: Wrong input!")

  



print(intro)
press_enter()
print("Let's start with your calculation...")
press_enter()

investment_type_request()

ETF()


