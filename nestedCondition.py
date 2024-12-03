# Find the largest of three numbers  
num1 = 12
num2 = 150
num3 = 50

if num1 >= num2:
        if num1 >= num3:
            print(num1)
        else:
            print(num3)
            
else:
    if num2 >= num3:
            print(num2)
    else:
            print(num3)


# Check leap year  
year = 2005
    
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
else:
        print("not leap year")


# Nested temperature check  
temp = 55
if temp < 15:
        print("Cold")
else:
        if temp <= 30:
            print("Warm")
        else:
            print("Hot")


# Vowel or consonant  
char = "$"
vowels = "aeiouAEIOU"
if len(char) == 1 and char.isalpha():
        if char in vowels:
            print("Vowel")
        else:
            print("Consonant")
else:
        print("Invalid input")



#Driving eligibility  
age = 12
if age >= 18:
    print( "Eligible to drive")
else:
     print("Not eligible to drive")

