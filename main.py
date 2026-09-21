# Global variable for calculating the annual return
a_rent = 0

# Opens the two .txt files and reads their content
with open("starttxt.txt", "r", encoding="utf-8") as file:
    intro = file.read()

with open("sources.txt", "r", encoding="utf-8") as file:
    sources = file.read()

# Function that requires the user to press Enter
def press_enter():
    input()

# Function that lets the user choose if they want to end the program
def Q():
    while True:
        Q = input("Do you want to quit the program? Y/n ").upper()
        if Q == "Y":
            print("You quit the program! Goodbye!")
            return True
        elif Q == "N":
            return False
        else:
            print("Please enter Y or N.")

# Function that lets the user compare all five different investment types
def compare_investment_methods():
    while True:
        try:
            a_rentb = float(
                input("Enter your annual rent available in your bank account! ")
            )
            if a_rentb < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative number.")

    while True:
        monthly_or_once = input(
            "Do you want to invest monthly or just once? "
            "Enter 1 = monthly 2 = one-time: "
        )
        if monthly_or_once in ("1", "2"):
            break
        print("Please enter 1 or 2.")

    while True:
        try:
            investment = float(input("Enter how much money you want to invest! "))
            if investment < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative number.")

    while True:
        try:
            years = int(input("How many years do you want to invest? "))
            if years <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive whole number.")

    print()
    print()
    print()

    c = 1
    a_rent = 0
    Result_of = ""

    while c < 6:
        if c == 1:
            a_rent = 0.08
            Result_of = "Result of MSCI World:"
        elif c == 2:
            a_rent = 0.10
            Result_of = "Result of S&P 500:"
        elif c == 3:
            a_rent = 0.07
            Result_of = "Result of Dax 40:"
        elif c == 4:
            a_rent = 0.06
            Result_of = "Result of SMI:"
        elif c == 5:
            a_rent = a_rentb / 100
            Result_of = f"Result of banking by an annual rent of {a_rentb}%:"

        if monthly_or_once == "1":
            monthly_rate = a_rent / 12
            months = years * 12
            total = 0.0

            for month in range(months):
                total = total * (1 + monthly_rate)
                total += investment

            all_monthly_investment = investment * months
        else:
            total = investment

            for i in range(years):
                total = total * (1 + a_rent)

            all_monthly_investment = investment

        only_annuel_rent_profit = total - all_monthly_investment

        print(Result_of)
        print(
            f"The value you made only from annual returns in {years} years is: "
            f"{round(only_annuel_rent_profit, 2)}"
        )
        print(f"The value in {years} years is: {round(total, 2)}")
        print()
        print()
        print()

        c += 1

# Calculation for the ETFs
def ETF():
    global a_rent

    while True:
        monthly_or_once = input(
            "Do you want to invest monthly or just once? "
            "Enter 1 = monthly 2 = one-time: "
        )
        if monthly_or_once in ("1", "2"):
            break
        print("Please enter 1 or 2.")

    while True:
        try:
            investment = float(input("Enter how much money you want to invest! "))
            if investment < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative number.")

    while True:
        try:
            years = int(input("How many years do you want to invest? "))
            if years <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive whole number.")

    if monthly_or_once == "1":
        monthly_rate = a_rent / 12
        months = years * 12
        total = 0.0

        for month in range(months):
            total = total * (1 + monthly_rate)
            total += investment

        # Calculates how much money was gained only from the annual return
        all_monthly_investment = investment * months
        only_annuel_rent_profit = total - all_monthly_investment

        print(
            f"The value you made only from annual returns in {years} years is: "
            f"{round(only_annuel_rent_profit, 2)}"
        )
        print(f"The value in {years} years is: {round(total, 2)}")
        Q()

    elif monthly_or_once == "2":
        total = investment

        for i in range(years):
            total = total * (1 + a_rent)

        # Calculates how much money was gained only from the annual return
        only_annuel_rent_profit = total - investment

        print(
            f"The value you made only from annual returns in {years} years is: "
            f"{round(only_annuel_rent_profit, 2)}"
        )
        print(f"The value in {years} years is: {round(total, 2)}")
        Q()

# Bank savings function that lets the user set their custom annual return from their bank account
def Bank_Savings():
    while True:
        try:
            a_rentb = float(
                input("Enter your annual rent available in your bank account! ")
            )
            if a_rentb < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative number.")

    while True:
        monthly_or_once = input(
            "Do you want to invest monthly or just once? "
            "Enter 1 = monthly 2 = one-time: "
        )
        if monthly_or_once in ("1", "2"):
            break
        print("Please enter 1 or 2.")

    while True:
        try:
            investment = float(input("Enter how much money you want to invest! "))
            if investment < 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid non-negative number.")

    while True:
        try:
            years = int(input("How many years do you want to invest? "))
            if years <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive whole number.")
    
    annual_rate = a_rentb / 100

    if monthly_or_once == "1":
        monthly_rate = annual_rate / 12
        months = years * 12
        total = 0.0
        all_monthly_investment = investment * months

        for month in range(months):
            total = total * (1 + monthly_rate)
            total += investment

        # Calculates how much money was gained only from the annual return
        only_annuel_rent_profit = total - all_monthly_investment

        print(
            f"The value you made only from annual returns in {years} years is: "
            f"{round(only_annuel_rent_profit, 2)}"
        )
        print(f"The value in {years} years is: {round(total, 2)}")
        Q()

    elif monthly_or_once == "2":
        total = investment

        for i in range(years):
            total = total * (1 + annual_rate)

        # Calculates how much money was gained only from the annual return
        only_annuel_rent_profit = total - investment

        print(
            f"The value you made only from annual returns in {years} years is: "
            f"{round(only_annuel_rent_profit, 2)}"
        )
        print(f"The value in {years} years is: {round(total, 2)}")
        Q()

# Menu that lets the user choose between different things the program can do
def investment_type_request():
    global a_rent

    while True:
        ITR = input(
            """Which investment method do you want to calculate?

        1. MSCI World
        2. S&P 500
        3. Bank Savings
        4. Dax 40
        5. SMI
        6. Compare Investment Methods
        7. Show Sources
        8. Quit

        Please enter your choice:
        """
        )

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
            compare_investment_methods()
        elif ITR == "7":
            print(sources)
        elif ITR == "8":
            print("You quit the program! Goodbye!")
            return
        else:
            print("Error: Wrong input!")

# Start of the program
print(intro)
press_enter()

investment_type_request()
