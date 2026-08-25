'''
Q1. Accept two numbers and print the greatest between them.

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))

if a > b:
    print(f"{a} is gretar than {b}")
else:
    print(f"{b} is gretar than {a}")
'''

'''
Q2. Accept the gender from the user as char and print the
respective greeting message
Ex - Good Morning Sir (on the basis of gender)


gender=input("Enter your gender :")

if gender == 'MALE' or gender == 'male':
    print("Good Morning Sir") 
else:
    print("Good morning mam")

'''
'''
Q3. Accept an integer and check whether it is an even number or odd.

number=int(input("Enter number :"))

if number % 2==0:
    print(f"{number} is Even")
else:
    print(f"{number} is odd")
'''
'''
Q4. Accept name and age from the user. Check if the user is a
valid voter or not.
Ex- “hello Adil you are a valid voter”

age=int(input("Enter your age :"))

if age >= 18:
    print("hello Adil you are a valid voter")
else:
    print("hello Adil you are Not a valid voter")

'''
'''
Q5. Accept a year and check if it a leap year

year=int(input("Enter a year :"))

if year%400==0 or(year%4==0 and year%100!=0):
    print("Leap year")
else:
    print("Not leap year")
'''