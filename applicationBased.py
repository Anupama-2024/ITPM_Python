#Season finder  

month = "January"
if month in ["December", "January", "February"]:
        print("Winter")
elif month in ["March", "April", "May"]:
        print("Spring")
elif month in ["June", "July", "August"]:
        print("Summer")
elif month in ["September", "October", "November"]:
        print("Autumn")
else:
        print("Invalid month")


#Password validation  
"""It must be at least 8 characters long and contain '@'"""
password = ""
    
if len(password) >= 8 and '@' in password:
        print("Password is valid.")
else:
        print("Password is invalid" )


#Categorize BMI  
bmi = 23
    
if bmi < 18.5:
        print("Underweight")
elif 18.5 <= bmi <= 24.9:
        print("Normal")
elif 25 <= bmi <= 29.9:
        print("Overweight")
elif bmi >= 30:
        print("Obese")
else:
        print("Invalid BMI")


#Character type checker  
char = ""
if char.isalpha():
        print("Alphabet")
elif char.isdigit():
        print("Digit")
else:
        print("Special Character")



#Electricity bill  
units = 250
    
if units <= 100:
        bill = units * 5
elif units <= 200:
        bill = (100 * 5) + (units - 100) * 10
else:
        bill = (100 * 5) + (100 * 10) + (units - 200) * 15
print( bill)