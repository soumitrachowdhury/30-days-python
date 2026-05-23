import math

#Welcome UI
print("\n-------WELCOME-------\n")

#Taking user preferences
print("Please select with unit of measurement you prefer \n 1. kg/cm \n 2. pounds/inches")

while True: #For option checking
        
    user_choice=int(input("\nOption: "))

    #Calculating BMI
    if user_choice == 1:
        while True:
            user_weight=input("Enter your weight (kg): ")
            user_height=input("Enter your height (cm): ") 
            
            #Checking user input type
            #replace(".","",1) -- removes the first "." to make it look like an integer data so that isdigit() can work
            if user_weight.replace(".","",1).isdigit() and user_height.replace(".","",1).isdigit():
                #Checking zero error
                if float(user_height) ==0 or float(user_weight) == 0:
                    print("Height or Weight can't be zero. Please enter the correct value.")
                else:
                    #Calculating BMI
                    result= float(user_weight)/(math.pow((float(user_height)/100),2))
                    break
            else:
                print("Only integer or float type data are allowed. Try again.\n")
        break
    
            
    elif user_choice == 2:
        while True:
            user_weight=input("Enter your weight (pound): ")
            user_height=input("Enter your height (inches): ") 
            
            #Checking user input type
            if user_weight.replace(".","",1).isdigit() and user_height.replace(".","",1).isdigit():
                #Checking zero error
                if float(user_height) ==0 or float(user_weight) == 0:
                    print("Height or Weight can't be zero. Please enter the correct value.")
                else:
                    #Calculating BMI
                    result= (float(user_weight)/(math.pow(float(user_height),2))) * 703 # Converting to International System of Units
                    break
            else:
                print("Only integer or float type data are allowed. Try again.\n")
        break

    else:
        print("Invalid choose. Please try again.\n")


print()

#Showing relevant output
if result < 18.5:
    print(f"Your BMI is {result:.2f} and you are Underweight")
elif 18.5<= result <= 24.9:
    print(f"Your BMI is {result:.2f} and you have a Normal weight")
elif 25.0<= result <= 29.9:
    print(f"Your BMI is {result:.2f} and you are Overweight")
else:
    print(f"Your BMI is {result:.2f} and you are Obese")

print()

