def is_leap_year(year):
    if year < 1000 or year > 9999:
        return "Please enter a 4 digit year."

    if (year % 4 == 0 and year % 100 != 0):
        return f"The year {year} is a Leap Year."
    else:
        return f"The year {year} is not a Leap Year."

user_input = input("Enter a 4 digit year: ")
year = int(user_input)
print(is_leap_year(year))