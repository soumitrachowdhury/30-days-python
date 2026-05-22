#Identifying current year
from datetime import date
current_year = date.today().year

#User invitation 
print("-----Please Answer this following question-----")

# Taking user responses and verifying input type 
user_name=input("Enter your name: ")
while True:
    if user_name.replace(" ","").isalpha():
        break
    else:
        user_name=input("Invalid data type. Please enter your name again: ")


user_age=input("What is your age: ")
while True:
    if user_age.isdigit():
        break
    else:
        user_age=input("Invalid data type. Please enter age again: ")

user_city=input("Enter the name of the city you live in: ")
while True:
    if user_city.replace(" ","").isalpha():
        break
    else:
        user_city=input("Invalid data type. Please enter city name again: ")

#Printing response
print(f"Hello {user_name}, you were born in {current_year - int(user_age)} and you live in {user_city}")