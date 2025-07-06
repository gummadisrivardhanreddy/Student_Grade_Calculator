def Student_grade():
    if percentage >=90:
        return "A+"
        
    elif percentage >=90:
        return "A"
        
    elif percentage >=80:
        return "B+"
        
    elif percentage >=70:
        return "B"
        
    elif Percentage >=60:
        return "c"
        
    elif percentage >=50:
        return "D"
        
    elif percentage >=40:
        return "E"
        
    else:
        return "F"
        
        
name = input("Enter your name: ")
subject = int(input("Enter number of subject: "))


marks = []
for i in range (subjects) :
    marks = float(input(f" Enter the marks of subjects {i+1}:"))
marks.append(marks)
total = sum(marks)
average = total / subjects 
percentage = (total / ( subjects * 100)*100)
grade = Student_grade(percentage)
print("\n -- Report card -- ")
print(f" Name : {name}")
print(f" Total marks : {total} / {subjects * 100}")
print(f" Average : {average}")
print(f" Percentage :{percentage}")
print(f" Grade : {grade}")
