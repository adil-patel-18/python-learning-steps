# Q1. Accept two numbers and print the greatest between them.
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))

if a > b:
    print(f"{a} is gretar than {b}")
else:
    print(f"{b} is gretar than {a}")


# Q2. Accept the gender from the user as char and print the respective greeting message
#Ex - Good Morning Sir (on the basis of gender)
gender=input("Enter your gender :")

if gender == 'MALE' or gender == 'male':
    print("Good Morning Sir") 
else:
    print("Good morning mam")


# Q3. Accept an integer and check whether it is an even number or odd.
number=int(input("Enter number :"))

if number % 2==0:
    print(f"{number} is Even")
else:
    print(f"{number} is odd")

# Q4. Accept name and age from the user. Check if the user is a
# valid voter or not.
# Ex- “hello Adil you are a valid voter”

age=int(input("Enter your age :"))

if age >= 18:
    print("hello Adil you are a valid voter")
else:
    print("hello Adil you are Not a valid voter")


# Q5. Accept a year and check if it a leap year

year=int(input("Enter a year :"))

if year%400==0 or(year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not leap year")

# Q6. Accept a number and check whether it is positive or negative.
number=int(input("Enter a number :"))
if number > 0:
    print("positive number")
else:
    print("negative number")


# Q7. Accept a number and check whether it is even or odd.
number=int(input("Enter a number :"))
if number % 2==0:
    print("Even number")
else:
    print("odd number")

# Q8. Accept three numbers and print the largest number.
num1=int(input("Enter number :"))
num2=int(input("Enter number :"))
num3=int(input("Enter number :"))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greter {num2} and {num3}")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is greter {num1} and {num3}")
else:
    print(f"{num3} is greter {num1} and {num2}")


#9. Accept a number and check whether it is divisible by both 5 and 11.
number=int(input("Enter a number :"))

if number%5==0 and number%11==0:
    print("divisible by both 5 and 11")
else:
    print("Not divisible by both 5 and 11")


# Q10. Accept a person's age and print:
# 0–12 → Child
# 13–19 → Teenager
# 20–59 → Adult
# 60+ → Senior Citizen
age=int(input("Enter your age :"))

if age > 0 and age <= 12:
    print("child")
elif age > 13 and age <= 19:
    print("Teenager")
elif age > 20 and age <= 59:
    print("Adult")
else:
    print("Senior Citizen")
