continue_response = 'yes' 

while continue_response == 'yes':
    # 1st input: 
    height = input("enter height in meters: ")
    # 2nd input: 
    weight = input("enter weight in kilograms: ")

    typechange_height= float(height)
    typechange_weight= int(weight)

    BMI = typechange_weight/(typechange_height*typechange_height)

    typechange_BMI = int(BMI)

    print("Your BMI is: ", typechange_BMI)
    continue_response = (input("Do you want to continue? type 'yes'/'no: '"))

