#Check even or odd  
num = 20
if num % 2 == 0:
    print("number is even")
else :
    print("number is odd")

#Check divisibility  
num = 50
if num % 3 == 0 and num % 5 == 0:
      print("The number is divisible by both 3 and 5") 
elif num % 3 == 0:
      print("The number is divisible by 3")
elif num % 5 == 0:
      print("The number is divisible by 5")
else:
      print("The number is not divisible by 3 or 5")

#Minimum of two numbers
num1 = 100
num2 = 25
if num1 < num2:
    print( "minimun number")
else :
     print("max")

# check no. is positive or negative

num = 34
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


 # Grade checker

percentage = 69
    
if 90 <= percentage <= 100:
        print("A")
elif 70 <= percentage < 90:
        print("B")
elif 50 <= percentage < 70:
        print("C")
elif 0 <= percentage < 50:
        print( "F")
else:
        print("Invalid percentage")
