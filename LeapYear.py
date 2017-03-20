def leapYear(year):
    if (year % 400) == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True


size = int(input("Enter the number of years: "))
years = []
print("\n Enter the years : \n")
for i in range(size):
    years.append(int(input()))

for year in years:
    if leapYear(year):
        print(year, " is a leap year.")
    else:
        print(year, " is not a leap year.")
