def show(n):#recursive function
    if n == 0: #basecase
        return
    print(n)
    show(n-1) #call its self
show(6) #function calls

def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)
    
print(fact(5))

'''
def sum(n):
    if n==0:
        return
    print(n)
    sum(n-1)+n
sum(5)
'''

def print_list(list,idx):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list,idx+1)
fruits = ["mango","apple","litchi",'banana']
print_list(fruits,0)


#                                                            Python Recursion practice.

# 🟢 Basic Level

#Q1. Create a recursive function to print numbers from **1 to 10**.
def number(n):
    if n == 10:
        return 
    print(n)
    number(n+1)
number(1)


#Q2.Create a recursive function to print numbers from **10 to 1**.
def number(n):
    if n == 0:
        return 
    print(n)
    number(n-1)
number(10)

# Q3. Create a recursive function to calculate the **sum of numbers from 1 to n**.
#Example: `n = 5 → 15`
def number(n):
    if n == 0:
        return 0
    return number(n-1)+n
    
print(number(10))

#Q4. Create a recursive function to calculate the **factorial of n**.
#Example: `5! → 120`
def number(n):
    if n == 1:
        return 1
    return number(n-1)*n
    
print(number(5))

'''
**Q5.** Create a recursive function to calculate **a number raised to a power**.
Example: `power(2, 4) → 16`

### 🟡 Intermediate Level

**Q6.** Create a recursive function to find the **sum of digits** of a number.
Example: `1234 → 10`

**Q7.** Create a recursive function to **count the digits** of a number.
Example: `12345 → 5`

**Q8.** Create a recursive function to **reverse a number**.
Example: `1234 → 4321`

**Q9.** Create a recursive function to find the **nth Fibonacci number**.
Example: `fibonacci(6) → 8`

**Q10.** Create a recursive function to find the **GCD/HCF of two numbers**.

### 🔴 Challenge Level

**Q11.** Create a recursive function to check whether a string is a **palindrome**.
Example: `"madam" → True`

**Q12.** Create a recursive function to find the **maximum element in a list**.

**Q13.** Create a recursive function to calculate the **sum of all elements in a list**.

**Q14.** Create a recursive function to count how many times a particular element appears in a list.
Example: `[1,2,2,3,2]`, search `2` → `3`

**Q15.** Create a recursive function to print all elements of a list **without using a loop**.

**Rule:** Har question mein **loop (`for`/`while`) use nahi karna**. Recursion use karni hai.

Pehle **Q1–Q5 solve karke bhejo**, main tumhe **marks + mistakes + corrected code** dunga.
'''