#                                                                 🟢 Level 1 — Basic `for` loop

# 1. 1 se 10 tak numbers print karo.
for i in range(1,11,1):
    print(i)

# 2. 10 se 1 tak reverse numbers print karo.

for i in range(10,0,-1):
    print(i)

# 3. 1 se 50 tak numbers print karo.
for i in range(1,51,1):
    print(i)

# 4. 1 se 100 tak even numbers print karo.
for i in range(2,101,2):
    print(i)

# 5. 1 se 100 tak odd numbers print karo.
for i in range(1,101,2):
    print(i)

# 6. 1 se 20 tak numbers ke squares print karo.
for i in range(1,21,1):
    print(i*i)

# 7. 1 se 10 tak numbers ke cubes print karo.
for i in range(1,21,5):
    print(i*i*i)

# 8. 1 se 100 tak 5 ke multiples print karo.
for i in range(1,100,10):
    print(i*5)

#9. 1 se 100 tak 10 ke multiples print karo.
for i in range(1,100,1):
    print(i*10)

# 10. 1 se 50 tak numbers ka sum find karo.
sum=0
for i in range(1,51,1):
    sum+=i
print(sum)

#                                                                     🟡 Level 2 — Logic Building

# 11. User se `n` input lo aur 1 se `n` tak print karo.
n=int(input("Enter a number :"))
for i in range(1,n+1,1):
    print(i)

# 12. User se `n` input lo aur 1 se `n` tak even numbers print karo.
n=int(input("Enter a number :"))
for i in range(1,n+1):
    if i%2==0:
        print(i)

# 13. User se `n` input lo aur 1 se `n` tak odd numbers print karo.
n=int(input("Enter a number :"))
for i in range(1,n+1):
    if i%2!=0:
        print(i)

# 14. 1 se `n` tak numbers ka sum find karo.
n=int(input("Enter a number :"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

# 15. 1 se `n` tak even numbers ka sum find karo.
n=int(input("Enter a number :"))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(sum)

# 16. 1 se `n` tak odd numbers ka sum find karo.
n=int(input("Enter a number :"))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum+=i
print(sum)

# 17. `n` ka multiplication table print karo.
n=int(input("Enter a number :"))
for i in range(n,n*11,n):
    print(i)

# 18. `n` ka factorial find karo.
n=int(input("Enter a number :"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print(factorial)

# 19. 1 se `n` tak numbers mein se 3 ke divisible numbers print karo.
n=int(input("Enter a number :"))
for i in range(1,n+1):
    if i%3==0:
        print(i)

# 20. 1 se `n` tak numbers mein se 3 aur 5 dono se divisible numbers print karo.
n=int(input("Enter a number :"))
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(i)

#                                                                      🟠 Level 3 — Strong Logic

# 21. Check karo ki `n` prime number hai ya nahi.
n=int(input("Enter a number :"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count == 2:
    print(f"{n} is prime number ")
else:
    print(f"{n} is not prime number ")
    
# 22. 1 se `n` tak saare prime numbers print karo.
n=int(input("Enter a number :"))
count=0
for i in range(1,n+1):
    if n%i==0 and i%1==0:
        print(i)
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
