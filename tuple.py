#                                                     🐍 Python Tuple — Practice Questions
'''
# 🟢 Basic Level

# 1. Create a tuple containing `10, 20, 30, 40, 50` and print it.
tuple = (10,20,30,40,50)
print(tuple)

# 2. Create a tuple of 5 names and print each element.
tuple=('adil','alfaiz','sameer','saif','abbas')
print(tuple)

# 3. Create a tuple and print the **first element**.
tuple=('adil','alfaiz','sameer','saif','abbas')
print(tuple[0])

# 4. Create a tuple and print the **last element** using negative indexing.
tuple=('adil','alfaiz','sameer','saif','abbas')
print(tuple[-1])

# 5. Find the **length** of a tuple using `len()`.
tuple=('adil','alfaiz','sameer','saif','abbas')
print(len(tuple))

# 6. Create a tuple and print elements from index `1` to `3`.
tuple=('adil','alfaiz','sameer','saif','abbas')
print(tuple[1:4])

# 7. Check whether `30` exists in the tuple.
tuple = (10,20,30,40,50)
if 30 in tuple:
    print("exists")
else:
    print("Not exists ")

# 8. Create a tuple containing duplicate values and count how many times `10` appears.
tuple = (10,20,30,40,50,10)
print(tuple.count(10))

# 9. Find the index of `30` using `index()`.
tuple = (10,20,30,40,50)
print(tuple.index(30))

# 10. Print all elements of a tuple using a `for` loop.
tuple = (10,20,30,40,50)
for i in tuple:
    print(i)


### 🟡 Practice Level

# 11. Create a tuple of numbers and print only **even numbers**.
tuple=(1,2,3,4,5,6,7,8,9,10)
for i in tuple:
    if i%2==0:
        print(i)

# 12. Create a tuple of numbers and print only **odd numbers**.
tuple=(1,2,3,4,5,6,7,8,9,10)
for i in tuple:
    if i%2!=0:
        print(i)

# 13. Find the **sum** of all numbers in a tuple.
tuple=(1,2,3,4,5,6,7,8,9,10)
sum=0
for i in tuple:
    sum+=i
print(sum)

# 14. Find the **maximum** number in a tuple.
tuple=(1,2,3,4,5,6,7,8,9,10)
print(max(tuple))

# 15. Find the **minimum** number in a tuple.
tuple=(1,2,3,4,5,6,7,8,9,10)
print(min(tuple))

# 16. Count how many times a given number appears in a tuple.
tuple=(1,2,3,4,5,6,7,8,9,10)
print(tuple.count(5))

# 17. Create a tuple of numbers and calculate how many numbers are greater than `50`.
tuple = (10,20,30,40,50,60,70)
count=0
for i in tuple:
    if i > 50:
        count+=1
print(count)

# 18. Create a tuple and print it in **reverse order**.
tuple=(1,2,3,4,5,6,7,8,9,10)
print(tuple[::-1])

#.19. Convert a list into a tuple.
list=[1,2,3,4,5,6,7,8,9,10]
tuple=tuple(list)
print(tuple)

# 20. Convert a tuple into a list.
tuple=(1,2,3,4,5,6,7,8,9,10)
list=list(tuple)
print(list)

'''
#                                                      🔵 Important Practice
'''
# 21. Create a tuple of student details:
text
(name, age, city, marks)
and print each value.
'''
tuple=('adil',20,'Latur',89)
for i in tuple:
    print(i)
'''
# 22. Take 5 numbers from the user, store them in a tuple, and print the tuple.
numbers=[10,20,30]
number=int(input("Enter a numbers :"))
numbers.append(number)
tuple1=tuple(numbers)
print(tuple1)

# 23. Take a number from the user and check whether it exists in a tuple.
tuple=(1,2,3,4,5,6)
number=int(input("Enter a numbers :"))
if number in tuple:
    print("exists")
else:
    print("not exists")

# 24. Find the second-largest number in a tuple.
tuple1=(1,2,3,4,5,6)

list1=list(tuple1)
list1.sort()
tuple2=tuple(list1)
print(tuple2[-2])
'''
# 25. Find the total number of even and odd numbers in a tuple.
number = (1,2,3,4,5,6,7,8,9,10)
odd=0
even=0
for i in number:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"{even} is even")
print(f"{odd} is odd")