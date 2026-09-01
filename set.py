#                                             🐍 Python Set — Practice Questions
#🟢 Basic Level

#Q1.Create a set containing 10, 20, 30, 40, 50 and print it.
set ={10,20,30,40,50}
print(set)

#Q2.Create a set of 5 fruits and print all elements.
set = {"apple","mango","banana","graps","adil"}
print(set)

#Q3.Create a set with duplicate values and observe the output.
set = {10,10,20,30,20,40,50}
print(set)

#Q4.Create an empty set and print it.
#my_set = set()
#print(my_set)

#Q5.Find the length of this set:
set = {10,10,20,30,20,40,50}
print(len(set))

#Q6.Add 60 to this set using add():

numbers = {10, 20, 30, 40, 50}
numbers.add(60)
print(numbers)

#Q7.Add 60, 70, 80 using update().
numbers = {10, 20, 30, 40, 50}
numbers.update([60,70,80])
print(numbers)


#Q8.Remove 30 using remove().
numbers = {10, 20, 30, 40, 50}
numbers.remove(30)
print(numbers)

#Q9.Remove 100 using discard() and observe what happens.
numbers = {10, 20, 30, 40, 50}
numbers.discard(100)
print(numbers)

#Q10.Use pop() to remove one element from a set.
numbers = {10, 20, 30, 40, 50}
numbers.pop()
print(numbers)

#Q11.Use clear() to remove all elements.
numbers = {10, 20, 30, 40, 50}
numbers.clear()
print(numbers)

#Q12.Create a copy of a set using copy().
numbers = {10, 20, 30, 40, 50}
number=numbers.copy()
print(number)

#Q12.Find the union of A and B.
A={1,2,3}
B={3,4,5}
print(A.union(B))

#Q13.Find the intersection of A and B.
A={1,2,3}
B={3,4,5}
print(A.intersection(B))

#Q14.Find the difference A - B.
A={1,2,3}
B={3,4,5}
print(A.difference(B))

#Q15.Find the difference B - A.
A={1,2,3}
B={3,4,5}
print(B.difference(A))

#Q16.Find the symmetric difference of A and B.
A={1,2,3}
B={3,4,5}
print(A.symmetric_difference(B))

#17.Check whether:A is a subset of B.
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))

#18.Check whether B is a superset of A.
A = {1, 2, 3}
B = {4, 5, 6}
print(A.issuperset(B))

#19.Check whether these two sets are disjoint:
A = {1, 2, 3}
B = {4, 5, 6}
print(A.isdisjoint(B))

#          ⭐ Challenge Questions

#Q20.Find common elements between two sets of student names.
A = {1, 2, 3,4}
B = {4, 5, 6}
print(A.intersection(B))

#Q21.Create two sets of numbers and find numbers present in the first set but not the second.
A = {1, 2, 3,4}
B = {4, 5, 6}
print(A.difference(B))

#Q22.Remove duplicate values from this list using a set:
'''numbers = [10, 20, 20, 30, 40, 40, 50, 50]

set1=set(numbers)
print(set1)
'''
'''
#Q23.Take two sets and print:
Union
Intersection
Difference
Symmetric Difference
'''
A = {1, 2, 3,4}
B = {4, 5, 6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

#24.Create a set of numbers from 1 to 10 and print only the even numbers using a for loop.
set = {1,2,3,4,5,6,7,8,9,10}

for i in set:
    if i%2==0:
        print(i)