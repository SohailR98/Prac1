from datetime import date

# ask user for date in yyyy-mm-dd format
user_date = input("Enter a date in yyyy-mm-dd format: ")

# convert user input to date object
date1 = date.fromisoformat(user_date)

# set date2 as current date
date2 = date.today()

# calculate the difference between the dates
delta = date2 - date1


# calculate the number of years, months, and days between the dates
years = delta.days // 365
months = (delta.days % 365) // 30
days = (delta.days % 365) % 30

# print the number of days, months, and years between the dates
print(f"{years} years, {months} months, and {days} days")
