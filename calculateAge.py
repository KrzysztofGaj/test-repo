from datetime import date

class age_z():
    months = {1: 'January', 2: 'February', 3: 'March',
              4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September',
              10: 'October', 11: 'November', 12: 'December'}

    def __init__(self, b_year, b_month, b_day):
        self.b_year = b_year
        self.b_month = b_month
        self.b_day = b_day

    def inputBdayDate():
        global date_b
        date_b = input("Enter date in YYYY-MM-DD format: ")
        year, month, day = map(int, date_b.split('-'))
        date_b = date(year, month, day)

def calculateAge(birthDate):
    days_in_year = 365.2425
    age = int((date.today() - birthDate).days / days_in_year)
    return age


jacek1 = age_z.inputBdayDate()

print(f'You are {calculateAge(date_b)} years old')
print(f'You were born on {date_b.day} {age_z.months[date_b.month]} {date_b.year}')