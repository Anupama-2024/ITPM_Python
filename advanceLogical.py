#Triangle validation  
a = 51
b = 51
c = 10

if a + b > c and a + c > b and b + c > a:
    print("It is a triangle")
else:
    print("Not a Triangle ") 



#Calculate tax based on salary  
salary = 5000000
if salary <= 500000:
    tax = salary * 0.05  # 5% tax rate
elif 500001 <= salary <= 1000000:
    tax = salary * 0.10  # 10% tax rate
else:
    tax = salary * 0.20  # 20% tax rate
print(tax)


# Categorize age  
age = 45
if 0 <= age <= 12:
        print("Child")
elif 13 <= age <= 19:
        print("Teen")
elif 20 <= age <= 59:
        print("Adult")
elif age >= 60:
        print("Senior")
else:
        print("Invalid age")


#Logical AND check  
num = 12
if num > 10 and num % 2 == 0:
        print("num is greater and divisible")
else:
        print("num is not greater and divisible")



#Logical OR check  
num = 133
if num < 5 or num > 20:
        print( True)
else:
        print(False)