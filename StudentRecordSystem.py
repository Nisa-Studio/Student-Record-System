#------------STUDENT RECORD SYSTEM---------------
students=[]

#for adding students to the list 
def Add_Student(student_id,student_name,age,department,GPA):
    student={"ID":student_id,
             "NAME":student_name,
             "AGE":age,
             "DEPARTMENT":department,
             "GPA":GPA
             }
    students.append(student)
    print("Student Added Successfully !!")
    print(students)
    return

#searching student in the list 
def searching_students(students,student_id):
    for s in students:                  
        if s["ID"]==student_id:
            print("Student Found!!")
            print("Name : ",s["NAME"]," , ",
                  "Id : ",s["ID"]," , ",
                  "Age : ",s["AGE"]," , ",
                  "Department : ",s["DEPARTMENT"]," , ",
                  "GPA : ",s["GPA"])
            return
       
    print("Student Not Found !!")

#displaying students from the list 
def displaying_students(students):
    if not students:
        print("LIST IS EMPTY")
        return
    else:
        for s in students:
            print("Name : ",s["NAME"]," , ",
                  "Id : ",s["ID"]," , ",
                  "Age : ",s["AGE"]," , ",
                  "Department : ",s["DEPARTMENT"]," , ",
                  "GPA : ",s["GPA"])
            

#deleting  student from the list
def deleting_student(students,student_id):
     for s in students:            
        if s["ID"]==student_id:
            students.remove(s)
            print("Student Deleted Successfully!!")
            return
      
     print("Student Not Found !!")

#updating student in the list 
def updating_student(students,student_id,new_department):   #for example if i wanna change the department 
     for s in students:            
        if s["ID"]==student_id:
          print("Previous Department= ",s["DEPARTMENT"])
          s["DEPARTMENT"]=new_department
          print("Student Data Updated Successfully!!")
          print("New Department= ",s["DEPARTMENT"])
          return
        
     print("Student Not Found !!")

#finding student with highest gpa
def highest_gpa(students):
    if not students:
        print("LIST IS EMPTY")
        return
    else:
        print("maximum GPA ")
        max_gpa=students[0]
        for s in students:
            if s["GPA"]>max_gpa["GPA"]:
                max_gpa=s
        print("Name : ",s["NAME"]," , ",
                  "Id : ",s["ID"]," , ",
                  "Age : ",s["AGE"]," , ",
                  "Department : ",s["DEPARTMENT"]," , ",
                  "GPA : ",s["GPA"])
                


Add_Student(17503,"Nisa Nayab",20,"Data Science",4)
Add_Student(17504,"Narin",21,"Computer Science",3.9)
Add_Student(17505,"Merjan",24,"Cyber Security",4)
print()
displaying_students(students)
print()
deleting_student(students,17504)
displaying_students(students)
print()
searching_students(students,17503)
print()
updating_student(students,17505,"AI")
print()
highest_gpa(students)