# Age Calculator

# Taking input from user
birth_year=int(input("Enter your birth year: "))
current_year=2026

age=current_year-birth_year #Current age calcualtion
months=age*12 # Age in months
days=age*365  # Age in days
hours=days*24 # Age in hours
minutes=hours*60 #Age in minutes
years_to_100=100-age

print("Current age: ",age)
print("Age in months: ",months)
print("Age in days: ",days)
print("Age in hours: ",hours)
print("Age in minutes: ",minutes)
print("Years until age 100: ", years_to_100)
