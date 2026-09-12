# practicing: **variables, input, operators, if-else, loops, strings, lists, tuples, sets, dictionaries, and functions**.
# 🟢 1. Variables & Input — Q1 to Q15

#1. Create a variable `name` and print it.
name="adil patel"
print(name)

#2. Create variables for your name, age, and city and print them.
name="adil patel"
city="Latur"
print(f"my name is {name} i am from {city}.")

#3. Take the user's name as input and print it.
name=input("Enter your name :")
print(name)

#4. Take two numbers as input and print them.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
print(num1,num2)

#5. Take your age as input and print it.
age=int(input("Enter your age :"))
print(age)

#6. Take name and age as input and display them in one sentence.
name=input("Enter your name :")
age=int(input("Enter your age :"))
print(f"My name is {name} age is {age}")

#7. Take two numbers and print their sum.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
print(num1+num2)


#8. Take three numbers and print their sum.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
num3=int(input("Enter two number :"))
print(num1+num2+num3)

#9. Take length and width as input and calculate rectangle area.
l=float(input("Enter length of area :"))
w=float(input("Enter width of area :"))
area=l*w
print(area)

#10. Take side of a square and calculate its area.
s=float(input("Enter side of area :"))
area=s**s
print(area)

#11. Take radius and calculate the area of a circle.
r=float(input("Enter radius of area :"))
pi=3.14
area=pi*r**2
print(area)

#12. Take marks of 5 subjects and calculate total marks.
mark1=int(input("Enter first number :"))
mark2=int(input("Enter first number :"))
mark3=int(input("Enter first number :"))
mark4=int(input("Enter first number :"))
mark5=int(input("Enter first number :"))
result=mark1+mark2+mark3+mark4+mark5
print(result)

#13. Take marks of 5 subjects and calculate average.
mark1=int(input("Enter first number :"))
mark2=int(input("Enter first number :"))
mark3=int(input("Enter first number :"))
mark4=int(input("Enter first number :"))
mark5=int(input("Enter first number :"))
result=mark1+mark2+mark3+mark4+mark5
print(result/5)

#14. Take price and quantity and calculate total amount.
product=int(input("Enter quantity :"))
price=float(input("Enter price :"))
calculate=product*price
print(calculate)

#15. Take temperature in Celsius and convert it to Fahrenheit.
f=int(input("Enter Fahrenheit :"))
c=(f*9/5)+32
print(c)


# 🟡 2. Operators — Q16 to Q30
16. Take two numbers and perform addition.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
print("addition is :",num1+num2)

#17. Perform subtraction of two numbers.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
print("addition is :",num1-num2)

#18. Perform multiplication of two numbers.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
print("addition is :",num1*num2)

#19. Perform division of two numbers.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
print("addition is :",num1/num2)

#20. Find the remainder using `%`.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
print("addition is :",num1%num2)

#21. Find the quotient using `//`.
num1=int(input("Enter two number :"))
num2=int(input("Enter two number :"))
print("addition is :",num1//num2)

#22. Calculate `5` raised to the power `3`.
num=5
power=num**3
print(power)

#23. Take a number and calculate its square.
num=int(input("Enter two number :"))
print(num**num)

#24. Take a number and calculate its cube.
num=int(input("Enter two number :"))
print(num**3)

#25. Calculate simple interest.
p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
si = (p * r * t) / 100
print(si)

#26. Calculate the perimeter of a rectangle.
l=float=input("Enter length of area :")
w=float=input("Enter width of area :")
area=2*(l+w)
print(area)

#27. Calculate the perimeter of a square.
w=float=input("Enter width of area :")
area=4*w
print(area)

#28. Calculate total bill including 10% discount.
bill=float=input("Enter length of area :")
discount=bill*0.10
final_bill = bill - discount
print(final_bill)

#29. Take two numbers and check whether they are equal.
l=float=input("Enter length of area :")
w=float=input("Enter width of area :")
if l == w:
    print("is equal")
else:
    print("not equal")
#30. Take two numbers and print which one is greater.
if l > w:
    print("l is greater")
elif w > l:
    print("w is greater")
else:
    print("Both are equal")
