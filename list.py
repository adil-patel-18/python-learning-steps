#                                                    🟢 Basic
# Create a list and print it.
list=[1,2,3,4,5,5]
print(list)

# Print the first element of a list.
print(list[0])

# Print the last element of a list.
print(list[-1])

# Find the length of a list.
print(len(list))

# Add an element to a list.
list.append(17)
print(list)

# Remove an element from a list.
list.remove(17)
print(list)

# Reverse a list.
list.sort(reverse=True)
print(list)

# Sort a list in ascending order.
list.sort()
print(list)

# Find the maximum number in a list.
print(max(list))

# Find the minimum number in a list.
print(min(list))


#                                              🟡 Medium
# Print all list elements using a for loop.
for i in list:
    print(i)

# Print all even numbers from a list.
for i in list:
    if i%2==0:
        print(i)

# Print all odd numbers from a list.
for i in list:
    if i%2!=0:
        print(i)

# Find the sum of all numbers in a list.
sum=0
for i in list:
    sum+=i
print(sum)

# Count how many times a number occurs.
print(list.count(5))

# Find the second largest number.
'''
list.sort()
print(list[-2])
'''
'''
Find duplicate elements.
'''

# Reverse a list without using reverse().
print(list[::-1])

# Find the largest number without using max().
for i in list:
    print(list[i])
'''
Find the smallest number without using min().
🔴 Advanced
Print all elements of a nested list.
Find the sum of all elements in a matrix.
Find the maximum element in a matrix.
Find common elements between two lists.
Remove duplicate values from a list.
Sort a list without using sort().
Find the second smallest number.
Find all prime numbers in a list.
Create a list of even numbers from 1 to 100 using list comprehension.
Convert a nested list into a single list.
📌 Most Important for Beginners

'''