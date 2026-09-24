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

#                                            🟢 3. If-Else — Q31 to Q50

# 31. Check whether a number is positive or negative
num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# 32. Check whether a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")


# 33. Check whether a number is even or odd.
num=int(input("Enter a number :"))
if num%2==0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#34. Check whether a person is eligible to vote.
age=int(input("Enter your age :"))
if age >= 18:
    print("person is eligible to vote")
else:
    print("person is Not eligible to vote")

#35. Check whether a person is eligible for a driving license.
age=int(input("Enter your age :"))
if age >= 18:
    print("person is eligible for a driving license")
else:
    print("person is Not eligible for a driving license")

#36. Check whether a student has passed or failed.
mark=float(input("Enter your marks :"))
if mark >= 35:
    print("pass")
else:
    print("Fail")

#37. Check whether marks are greater than 50.
mark=[78,58,98,65,85,97,45,20,30]
for i in mark:
    if i >= 50:
        print(i)
#38. Find the greater of two numbers.
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
if num1 > num2:
    print(f"{num1} is greter then {num2}")
elif num2 > num1:
    print(f"{num2} is greter then {num1}")
else:
    print("Both are equal")
#39. Find the largest of three numbers.
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter thered number"))
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is greter then {num2} and {num3}")
elif num1 >= num2 and num1 >= num3:
    print(f"{num2} is greter then {num1} and {num3}")
else:
    print(f"{num3} is greter then {num2} and {num3}")

#40. Find the smallest of three numbers.
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter thered number"))
if num1 <= num2 and num1 <= num3:
    print(f"{num1} is smallest")
elif num1 <= num2 and num1 <= num3:
    print(f"{num2} is smallest ")
else:
    print(f"{num3} is smallest ")

#41. Check whether a number is divisible by 5.
num=int(input("Enter a number :"))
if num%5==0:
    print(f"{num} is divisible by 5 ")
else:
    print(f"{num} is not divisible by 5")

#42. Check whether a number is divisible by both 5 and 10.
num=int(input("Enter a number :"))
if num%5==0 and num%10==0:
    print(f"{num} is divisible by 5 and 10")
else:
    print(f"{num} is not divisible by 5 and 10")

#43. Check whether a person is a child, adult, or senior citizen.
age=int(input("Enter your age :"))
if age < 18:
    print("child")
elif age < 60:
    print("adult")
else:
    print("senior citizen")

#44. Create a grade system using marks.
mark=int(input("Enter your marks :"))
if mark > 90:
    print("A+")
elif mark < 90 and mark > 80:
    print("A")
elif mark < 80 and mark > 70:
    print("B")
elif mark < 70 and mark > 60:
    print("C")
elif mark < 60 and mark > 50:
    print("D")
elif mark < 40 and mark > 35:
    print("E")
else:
    print("F")

#45. Create an age-based ticket price program.
age=int(input("Enter your age :"))
if age <= 5:
    result=100
elif age > 5 and age < 18:
    result=200
else:
    result=250
print(result)

#46. Check whether a year is a leap year.
# 46. Check whether a year is a leap year
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

# 47. Check whether a character is a vowel or consonant.
str=input("Enter character :")
vowel="aeiou"

if vowel in str:
    print("Vowel")
else:
    print("alphabat")

#48. Check whether a number is between 10 and 50.
num=int(input("Enter a number :"))
if num > 10 and num <= 50:
    print("number is between 10 and 50")
else:
    print("number is not between 10 and 50")

# 49. Check whether a student is eligible for an exam based on attendance.
days=int(input("Enter your attendance :"))
if days >= 80:
    print("eligible for an exam")
else:
    print("Not eligible for an exam")

#50. Create a simple login program using username and password.
username1=input("Enter username :")
password1=input("Enter password :")

username='adilpatel'
password='adil123'

if username1 == username and password1 == password:
    print("login sucsessful")
else:
    print("invalid password and username")
#                                                  🔵 4. For Loop — Q51 to Q70
#51. Print numbers from 1 to 10.
for i in range(1,11):
    print(i)

#52. Print numbers from 10 to 1.
for i in range(10,0,-1):
    print(i)

#53. Print even numbers from 1 to 20.
for i in range(2,21,2):
    print(i)

#54. Print odd numbers from 1 to 20.
for i in range(1,21,2):
    print(i)

#55. Print numbers from 1 to 50.
for i in range(1,51,1):
    print(i)

#56. Print multiples of 5 from 1 to 50.
for i in range(1,51,1):
    print(i*5)

#57. Print the multiplication table of 5.
for i in range(5,51,5):
    print(i)

#58. Take a number and print its multiplication table.
n=int(input("Enter a number :"))
for i in range(n,n*11,n):
    print(i)

#59. Calculate the sum of numbers from 1 to 10.
sum=0
for i in range(1,11):
    sum+=i
print(sum)

#60. Calculate the sum of numbers from 1 to `n`.
n=int(input("Enter a number :"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#61. Calculate the sum of even numbers from 1 to 50.
count=0
for i in range(1,51):
    if i%2==0:
        count+=i
print(count)

#62. Calculate the sum of odd numbers from 1 to 50.
count=0
for i in range(1,51):
    if i%2!=0:
        count+=1
print(count)

#63. Print squares of numbers from 1 to 10.
for i in range(1,11):
    print(i*i)

#64. Print cubes of numbers from 1 to 10.
for i in range(1,11):
    print(i**3)

#65. Count numbers from 1 to 100 divisible by 5.
count=0
for i in range(1,101):
    if i%5==0:
        count+=1
print(count)

#66. Print all numbers divisible by 3 between 1 and 50.
for i in range(1,51):
    if i%3==0:
        print(i)

#67. Print each character of a string.
str="Adil Azeem Patel"
for i in str:
    print(i)

#68. Count the characters in a string using a loop.
count=0
str="Adil Azeem Patel"
for i in range(len(str)):
    if i != -1:
        count+=1
print(count)

#69. Count vowels in a string using a loop.
count=0
vowel='aeoui'
str="Adil Azeem Patel"
for i in str:
    if i in vowel:
        count+=1
print(count)

#70. Find the factorial of a number using a loop.
fact=1
for i in range(1, 6):
    fact = fact * i
print(fact)

                                          # 🟣 6. Strings — Q86 to Q105
#86. Take a string and print its length.
str="Adil Patel"
print(len(str))

#87. Print the first character of a string.
print(str[0])

#88. Print the last character of a string.
print(str[-1])

#89. Print a string in uppercase.
print(str.upper())

#90. Print a string in lowercase.
print(str.lower())

#91. Count vowels in a string.
str="adil Patel"
vowel='aeiou'
count=0
for i in str:
    if i in vowel:
        count+=1
print(count)

#92. Count consonants in a string.
str="adil Patel"
vowel='aeiou'
count=0
for i in str:
    if i not in vowel:
        count+=1
print(count)

#93. Count spaces in a string.
str="adil Patel Azeem"
vowel=' '
count=0
for i in str:
    if i in vowel:
        count+=1
print(count)

#94. Count a particular character in a string.
print(str.count("a"))

#95. Check whether a string contains the letter `a`.
str="adil Patel Azeem"
space=' '
char='a'
con=0
for i in str:
    if i in char and i != space:
        con=con = i
print(con)

#96. Reverse a string.
str="adil Patel Azeem"
print(str[::-1])

#97. Check whether a string is palindrome.
str='aba'
a=str
rev=str[::-1]
if a==rev:
    print("palindrome")
else:
    print("not palindrome")

#98. Remove spaces from a string.
str="adil Patel Azeem"
print(str.replace(' ',''))

#99. Replace a word in a string.
str="adil Patel Azeem"
print(str.replace('adil','iqra'))

#100. Split a sentence into words.
list='adil iqra patel'
print(list.split())

#101. Join a list of words into a string.
list=['adil','iqra']
print(" ".join(list))

#102. Count the number of words in a sentence.
str='my name is adil patel'
space=' '
count=0
for i in str:
    if i not in space:
        count+=1
print(count)

#103. Find the longest word in a sentence.
#104. Print each word of a sentence on a new line.
str='my name is adil patel'
next=0
space=' '
for i in str:
    print(i,end="")
    if i == space:
        print("")
    
#105. Count uppercase and lowercase characters in a string.
str="adil Patel Azeem"
upper1=0
lower1=0
space1=0
d=' '
upper=str.upper()
for i in str:
    if i in upper and i not in d:
        upper1+=1
    elif i not in upper and i not in d:
        lower1+=1
    else:
        space1+=1    

print(f"upper charecter is {upper1}.\nlower charecter is {lower1}.\nspace is {space1}")

# 🟤 7. Lists — Q106 to Q120

#106. Create a list of 5 numbers and print it.
list=[1,2,3,4,5]
print(list)

#107. Print the first element of a list.
print(list[0])

#108. Print the last element of a list.
print(list[-1])

#109. Add an element using `append()`.
list.append(6)
print(list)

#110. Insert an element using `insert()`.
list.insert(2,7)
print(list)

#111. Remove an element using `remove()`.
list.remove(4)
print(list)

#112. Remove the last element using `pop()`.
list.pop()
print(list)

#113. Sort a list.
print(list.sort())

#114. Reverse a list.
print(list.sort(reverse=True))

#115. Find the largest number  `max()`.
print(max(list))

#116. Find the smallest number  `min()`.
print(min(list))

#117. Find the sum of a list  `sum()`.
print(sum(list))

#118. Count even numbers in a list.
even=0
for i in list:
    if i%2==0:
        even+=1
print(even)

#119. Count odd numbers in a list.
odd=0
for i in list:
    if i%2!=0:
        odd+=1
print(odd)

#120. Create a new list containing only numbers greater than 50.
list=[10,20,30,40,50,60,70]
for i in list:
    if i > 50:
        print(i)

