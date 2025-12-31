class Student():
    student={}
    
    def add_student(sid,name,n):

        Student.student[sid]={"Name":name,'Subjects':{}}

        for i in range(n):
            marks=[]
            Subjects = input("Enter Subject")
            print("--------------------------------------")
            for j in range (3):
                marks.append(int(input("Enter marks:")))
                Student.student[sid]["Subjects"][Subjects]=marks
        
    def Calculations(sid,sub):
        if sid in Student.student:
            print("Total:",sum(Student.student[sid]["Subjects"][sub]))
            avg = sum(Student.student[sid]["Subjects"][sub])/len(Student.student[sid]['Subjects'][sub])
            print("Average:",avg)
            return avg
            grade(avg)
        
        else:
            print("Re-Enter the Student_id")
            
    def grade(avg):
        if avg >=80:
            print('A')
           
        elif avg<80 and avg>=60:
            print('B')

        elif avg<60 and avg>=40:
            print('C')
        
        else:
            print("D")
        
    def display():
        print(Student.student)
        
Student.student={}
while True:
    print("==MENU==")
    print("1. Add Student")
    print("2.Student Report")
    print("3. Display")
    print("4.Exit")
    n=int(input("Enter your choice : "))
    if n == 4:
        print("Exiting System..")
        break 
    elif n==1:
        sid = int(input("Enter your Student-id:  "))
        name=input("Enter your Name: ")
        n=int(input("Enter no. of Subjects you have: "))
        Student.add_student(sid,name,n)
        
    elif n==2:
        print("--Student Report--")
        sid=int(input("Enter the student id :"))
        sub=input("Enter the subject name: ")
        Student.Calculations(sid,sub)
    
    elif n==3:
        print("--Students Details--")
        Student.display()
        
    else:
        print("Invalid Choice!")
        
