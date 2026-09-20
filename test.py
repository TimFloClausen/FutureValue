anuelrent = 0.07
monthly_investment = 100
years = 10



anuelrent = anuelrent /12


m = years * 12

all_investment = 100 * m




anuelrent += 1
anuelrent1_PO_m = anuelrent ** m
anuelrent1_PO_m -= 1

anuelrent -= 1


result = anuelrent1_PO_m / anuelrent
result *= monthly_investment
result -= all_investment
print(result)
