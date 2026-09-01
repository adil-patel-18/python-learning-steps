#                             🐍 Python Dictionary — Practice Questions
#🟢 Basic Level
'''
Q1. Create a dictionary containing:

name
age
city

Print the dictionary.
'''

student = {
    'name':'adil',
    'age':20,
    'city':'pune'
}
print(student)

#Q2. Create a dictionary of 5 students and their marks. Print it.
student = {
    'name':['adil','zishan','ali','saif','abbas'],
    'marks':[87,58,45,25,65]
}
print(student)

# Q3. Access and print the value of "name" from:
print(student['name'])

#Q4. Access "age" using the get() method.
print(student.get('age'))

#Q5. Add a new key "email" to the dictionary.
student['email']='adil@gmail.com'
print(student)
'''
#Q6. Change the value of "age" from 20 to 21.
student['age']=22
print(studetn)
'''
#Q7. Use update() to add "course": "B.Sc CS".
student.update({
    'course':"B.Sc CS"
})
print(student)

#Q8. Use pop() to remove "city".
#print(student.pop('city'))

#Q9. Use popitem() to remove the last item.
print(student.popitem())
print(student)

#Q10. Use clear() to remove all items.
student.clear()
print(student)

#Q11. Create a copy of a dictionary using copy().
copy=student.copy()
print(copy)

#Q12. Print all keys using keys().
print(student.keys())

#Q13. Print all values using values().
print(student.values())

#Q14. Print all key-value pairs using items().
print(student.items())

student = {
    "name": "Adil",
    "age": 20,
    "marks": 85,
    "city": "Latur"
}

#Q15. Print only the keys.
print(student.keys())

#Q16. Print only the values.
print(student.values())

#Q17. Print each key and value using a for loop.
print(student.items())

#Q18. Check whether "marks" exists in the dictionary.
print('marks' in student)


#Q19. Add "grade": "A" to the dictionary.
student['grade']='A'
print(student)

#Q20. Update "marks" from 85 to 90.
student['marks']=90
print(student)

#  🔴 Challenge Questions

#Q21. Create a dictionary containing 5 subjects and their marks. Find the total marks using a loop.
total=0
subjects = {
    'marks':[10,20,30,40,50]
}
for i in subjects['marks']:
    total+=i
print(total)

#Q22. Create a dictionary of 5 students and their marks. Print students who scored more than 50.
subjects = {
    'marks':[10,20,30,40,50,60,70]
}
for i in subjects['marks']:
    if i > 50:
        print(i)

#Q23. Create a dictionary and count how many key-value pairs it contains.
'''
count=0
student = {
    "name": "Adil",
    "age": 20,
    "marks": 85,
    "city": "Latur"
}
for i in student:
    count+=i
print(count)
'''
#Q24. Create a dictionary of numbers and their squares:
number={
    'squares':[1,2,3,4]
}
for i in number['squares']:
    print(i*i)

#Q25. Create a dictionary from two lists:
number={
    'squares':[1,2,3,4]
}
list1=list(number)
print(list1)