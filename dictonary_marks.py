def calculate_avg(m1,m2,m3):
    total=m1+m2+m3
    return total/3
def grade(avg):
 
    if avg>=90:
        return "A"
    elif avg>=75 and avg<=89:
        return "B"
    elif avg>=60 and avg<=74:
        return "C"
    else :
        return "F"
 
 
students={}
for i in range(5):
    name=input(f"enter the name of student{i}")
    marks=[]
    for j in range(3):
        mark=int(input(f"enter the marks {j}"))
        marks.append(mark)
    students[name]=marks
    for student,marks in students.items():
        print(student,':',marks)
        avg=calculate_avg(marks[0],marks[1],marks[2])
        grade=grade(avg)
        print(student,':',avg,':',grade)
    top_student=max(students,key=students.get)
    print(top_student)
