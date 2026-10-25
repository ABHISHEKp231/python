#looping through list
l=[1,2,4,5,6,7,8,9,10]
total=0
for num in l:
    total+=num
    print(num,end=" ")

total=0
for num in range(1,11):
    total+=num
print("the sum from 1 to 10 is:",num)

#dubling num in list
l=[1,2,3,4,5]
dl=[]
for num in l:
    dl.append(num*2)
    print(dl)
#item printing
foods = ["Dosa", "Idli", "Vada", "Bisibelebath"]

for food in foods:
    print(f"I like {food}")
#looping through dictionary convert dictionary to tuple 
student_marks={"annad":54,"geetha":23,"raju":45}
for student,marks in student_marks.items():
    print(f"{student}-{marks}")
#conver list to dictionary
students=["Abhi","rahul","ajith","ragu"]
marks=[23,78,90,56]
student_marks={}
for index,student in enumerate(students):
    student_marks[student]=marks[index]
print(student_marks)
# or using above one in range format
students=["Abhi","rahul","ajith","ragu"]
marks=[23,78,90,56]
student_marks={}
for i in range (len(students)):
    student_marks[students[i]]=marks[i]
print(student_marks)