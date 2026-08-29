'''
22. 1 se `n` tak saare prime numbers print karo.
n=int(input("Enter n :"))
for num in range(2,n+1):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count == 2:
        print(num)
'''
'''
23. `n` ke saare factors print karo.
24. `n` ke factors ki total count find karo.
25. 1 se `n` tak perfect numbers print karo.
26. Fibonacci series ke first `n` terms print karo.
27. 1 se `n` tak numbers mein largest number find karo.
28. 1 se `n` tak numbers mein smallest number find karo.
29. 1 se `n` tak numbers mein kitne even aur kitne odd hain, count karo.
30. 1 se `n` tak numbers mein 7 kitni baar aata hai, count karo.

### 🔥 Level 4 — Challenge

31. `n` ka reverse find karo using `for` loop.
32. `n` palindrome number hai ya nahi check karo.
33. `n` Armstrong number hai ya nahi check karo.
34. 1 se `n` tak Armstrong numbers print karo.
35. 1 se `n` tak palindrome numbers print karo.
36. 1 se `n` tak perfect numbers print karo.
37. `n` ke digits ka sum find karo.
38. `n` ke digits ka product find karo.
39. `n` mein total digits count karo.
40. `n` mein largest digit find karo.

'''

# Nested loop use karke 3 rows aur 5 columns mein * print karo.
'''
    for i in range(1,6):
        for j in range(1,4):
            print("*",end=" ")
        print("\n")
'''
# Nested loop se 1 se 5 tak numbers har row mein print karo.
'''
for i in range(6):
    for j in range(1,6):
        print(j,end=" ")
    print("\n")
'''
#Nested loop se 1–5 ka multiplication table print karo.
'''
for i in range(1,6):
    for j in range(1,11):
        print(i*j,end=" ")
    print(" ")
'''
# Nested loop se 1 se 3 tak square pattern print karo
'''
for i in range(1,4):
    for j in range(1,4):
        print(j*i)
'''
# Nested loop se 5 × 5 stars print karo.
'''
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print(" ")
'''
# Nested loop se ye pattern print karo
'''
*
**
***
****
*****
'''
'''
for i in range(6):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
'''
# Nested loop se ye pattern print karo
'''
12345
12345
12345
12345
12345
'''
'''
for i in range(5):
    for j in range(1,6):
        print(j,end=" ")
    print()
'''
# Nested loop se 1 se 5 tak multiplication tables print karo
'''
for i in range(1,11):
    for j in range(1,6):
        print(j*i,end=" ")
    print()
'''
# Ye pattern print karo:
'''
1
12
123
1234
12345
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print("")
'''
#Ye pattern print karo:
'''
*****
****
***
**
*
'''
'''
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()
'''
# Nested loop se 1 se 10 tak numbers ko rows mein print karo:
'''
1
2 3
4 5 6
7 8 9 10
'''
'''
num=1
for i in range(1,5):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print()
'''
# Nested loop se 1 se n tak prime numbers print karo.
'''
n=int(input("Enter a number :"))
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count == 2:
        print(i)
'''
# Nested loop se 1 se 100 tak even numbers print karo.
j=2
for i in range(1,101):
    while j <= i:
        if j%2==0:
            print(j,end="")