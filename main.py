continue_response = 'yes' 

while continue_response == 'yes':
    # 1st input: 
    height = input("enter height in meters: ")
    # 2nd input: 
    weight = input("enter weight in kilograms: ")

    typechange_height= float(height)
    typechange_weight= int(weight)

    BMI = typechange_weight/(typechange_height*typechange_height)
    if BMI < 18.5:
        print(f"Your BMI is {BMI}, you are underweight.")
    elif BMI > 18.5:
        if BMI <25:
            print(f"Your BMI is {BMI}, you have a normal weight.")
        elif BMI >= 25:
            if BMI < 30:
                print(f"Your BMI is {BMI}, you are slightly overweight.")
            elif BMI >= 30:
                if BMI< 35:
                    print(f"Your BMI is {BMI}, you are obese.")
                else:
                    print(f"Your BMI is {BMI}, you are clinically obese.")
        


    continue_response = (input("Do you want to continue? type 'yes'/'no: '"))

