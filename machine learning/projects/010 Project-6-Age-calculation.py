def calculate_age(year, month, date):
    import datetime
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(year,month,date)
    age = int((today-date_of_birth).days/365.25)
    print(age)

calculate_age(2022,6,1)