#                                                            🐍 Python Functions — Practice Questions

# 🟢 Basic Level

#Q1.Create a function `greet()` that prints `"Hello, Python"`.
def greet():
    print("Hello,python")
greet()

#Q2. Create a function `welcome(name)` that prints:
#text
#Welcome Adil
def welcome(name):
    print("Welcome ",name)

welcome('Adil')

#Q3. Create a function `add(a, b)` that prints the sum of two numbers.
def sum(a,b):
    sum=a+b
    print(sum)
sum(2,4)

#Q4. Create a function `square(n)` that returns the square of a number.
def square(n):
    return n*n
seqr=square(6)
print(seqr)

#Q5. Create a function `even_odd(n)` that checks whether a number is even or odd.
def even_odd(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
even=even_odd(7)
print(even)


# 🟡 Medium Level

#Q6.Create a function `maximum(a, b)` that returns the greater number.
def maximum(a,b):
    if a > b:
        return a 
    else:
        return b 
maxi=maximum(3,6)
print(maxi)

#Q7.Create a function `calculate(a, b)` that returns:
#* Addition
#* Subtraction
#* Multiplication
#* Division
def calculate(a,b):
    print('Addition',a+b)
    print('Subtraction',a-b)
    print('Multiplication',a*b)
    print('Division',a/b)
calculate(2,4)

#Q8.Create a function `factorial(n)` that returns the factorial of a number.
def factorial(n):
    fact=1
    for i in range(1,n+1,1):
        fact=fact*i 
    print(fact)
factorial(7)


#Q9.Create a function `count_vowels(text)` that counts the number of vowels in a string.
def count_vowels(text):
    count=0
    vowels='aieou'
    for i in text:
        if i in vowels:
            count=count+1
    print(count)
count_vowels('adil')

#Q10. Create a function `sum_list(numbers)` that returns the sum of all elements in a list.
def sum_list():
    list=[1,2,3,4,5,6]
    sum=0
    for i in list:
        sum=sum+i 
    print(sum)
sum_list()

#                                                    🔵 Function Types Practice

#Q11. Write a function with **no argument and no return value** that prints your name.
def name1(**name):
    print(name)
name1(name='adil')

#Q12.** Write a function with **argument but no return value** that prints the cube of a number.
def number(*cube):
    for i in cube:
        print(i**i)

number(1,2,3,4,5)

#Q13. Write a function with **no argument but with return value** that returns your age.

'''
**Q14.** Write a function with **argument and return value** that returns the average of three numbers.

---

### 🔴 Challenge

**Q15.** Create a function `is_prime(n)` that checks whether a number is prime.

**Q16.** Create a function `reverse_string(text)` that returns the reversed string.

**Q17.** Create a function `largest(numbers)` that finds the largest number in a list **without using `max()`**.

**Q18.** Create a function `count_even(numbers)` that counts how many even numbers are present in a list.

**Q19.** Create a function `remove_duplicates(numbers)` that returns a list without duplicate values.

**Q20.** Create a function `student_result(marks)` that calculates the total, percentage, and grade.
'''