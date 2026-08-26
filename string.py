# 1. Accept a string and print it.
str="Hello world"
print(str)

# 2. Accept your name and print `"Hello, <name>"`.
name="Adil patel"
print("Hello",name)

# 3. Accept a string and find its length.
str="Adil patel"
print(len(str))

# 4. Accept a string and print its first character.
str="Adil patel"
print(str[0])

# 5. Accept a string and print its last character.
str="Adil patel"
print(str[-1])

# 6. Accept a string and print the first 3 characters.
str="Adil patel"
print(str[0:3])

# 7. Accept a string and print the last 3 characters.
str="Adil patel"
print(str[-4:-1])

# 8. Accept a string and convert it to uppercase.
str="Adil patel"
print(str.upper())

# 9. Accept a string and convert it to lowercase.
str="Adil patel"
print(str.lower())

# 10. Accept a string and convert the first letter to uppercase.
str="adil patel"
print(str.capitalize())

# 11. Accept a string and count how many times `"a"` occurs.
str="Adil patel"
print(str.count('a'))

# 12. Accept a string and check if it contains `"python"`.
str='i am today learning java'
if 'python' in str:
    print("Python is present")
else:
    print("Python is not present")

# 13. Accept a string and check whether it starts with `"A"`.
str="Adil patel"
if str[0] == 'A':
    print("starts with A")
else:
    print("Not starts with A") 

# 14. Accept a string and check whether it ends with `"ing"`.
str="Adil patel"
print(str.endswith('ing'))

# 15. Accept a string and replace `"Python"` with `"Java"`.
str='i am today learning python'
print(str)
print(str.replace('python','java'))

# 16. Accept a string and remove spaces from the beginning and end.
name = input("Enter string: ")
print(name.strip())

# 17. Accept a string and count the number of spaces.
str="my name is adil patel"
count=0
for i in str:
    if i == " ":
        count+=1
print(count)

# 18. Accept a string and reverse it.
str="Adil patel"
print(str[::-1])

 #  19. Accept a string and check whether it is a palindrome.
str='apa'
rev=str[::-1]
if str == rev:
    print("it is a palindrome.")
else:
    print("it is Not palindrome")


# 20. Accept a string and print each character using a `for` loop.
str="Adil patel"
for i in str:
    print(i)

# 21. Count vowels (`a, e, i, o, u`) in a string.
str="adil patel"
count=0
vowels='aeiou'
for i in str:
    if i in vowels:
        count+=1
print(count)

# 22. Count consonants in a string.
str="adil patel"
count=0
vowels='aeiou'
for i in str:
    if i not in vowels:
        count+=1
print(count)

# 23. Count digits in a string.
str="adil 45patel"
count=0
digit='0123456789'
for i in str:
    if i in digit:
        count+=1
print(count)


# 24. Count uppercase letters in a string.
name=input("Enter your name :")
count=0
cap=name.upper()
for i in name:
    if i in cap:
        count+=1
print(count)

# 25. Count lowercase letters in a string.
name=input("Enter your name :")
count=0
cap=name.lower()
for i in name:
    if i in cap:
        count+=1
print(count)
