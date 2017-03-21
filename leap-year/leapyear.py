size = int(input("Enter the number of years: "))
years = []
print("\n Enter the years : \n")
for i in range(size):
    eachyear=(int(input()))
    years.append(eachyear)


def leapyear(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True


for year in years:
    if leapyear(year):
        print(year, " is a leap year.")
    else:
        print(year, " is not a leap year.")
