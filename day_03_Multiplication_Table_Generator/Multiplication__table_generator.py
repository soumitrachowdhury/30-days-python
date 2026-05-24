import random
#Welcoming user and taking input
print("\n----------Welcome User----------\n")

#Checking user input type
while True:
    user_data=input("Enter the integer number which multiplication table you want to see: ")
    if user_data.isdigit():
        break
    else:
        print("Invalid datatype! Only integer data type are allowed. Please try again.")

#Showing multiplication table
print(f"\nThe multiplication table for {user_data} is below: \n")
for i in range(10):
    print(f"{user_data}x{i+1}={int(user_data)*(i+1)}")

#Testing user knowledge
print("\nLet's play a multiplication result guessing game. \n")
num_one=random.randint(1,10) # random number between 1 to 10
num_two=random.randint(1,10)

#Checking user choose
print(f"What is {num_one} x {num_two} ?")
result=num_one*num_two
while True:
    user_response=int(input("Your answer: "))
    if user_response == result:
        print("\nCongratulation!! Your answer is Correct.\n")
        break
    else: 
        print("\nSorry but your answer is wrong. Please try again.")