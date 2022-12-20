from operator import truediv
from statistics import median


class Student_Record():
    def __init__(self,name,rollNo,maths,cse,science):
        #print('One Student Record Created...')
        self.name = name
        self.rollNo = rollNo
        self.maths = maths
        self.cse = cse
        self.science = science
        self.mean = (float(maths+cse+science))/3
        self.median= median([maths,cse,science])
        self.total = (maths+cse+science)

    def __lt__(self,other):
        if(self.total>other.total):
            return True
        else:
            return False


# LIST FOR RECORD OF STUDENTS
Slist = []

n = 10 #number of students
# 1. Take user input for number of students (at least 10 student’s data)
for i in range(0,n):
    name =       input('Enter   the   NAME: ')
    rollNo = int(input('Enter the ROLLNO: '))
    maths =  float(input('     MATHS Marks: '))
    cse  =   float(input('       CSE Marks: '))
    science =float(input('   SCIENCE Marks: '))
    Slist.append(Student_Record(name,rollNo,maths,cse,science))
# 2. Build the data structure by taking input from user


print('')
# 3. Display the list of users and their roll number on screen
print('\tName\tRollNO')
for i in range(0,n):
    print('\t'+Slist[i].name+'\t'+str(Slist[i].rollNo))
print('')

# 4. Ask the user to input name/or roll number based on display.
input = input('Enter the NAME/ROLLNO of Student: ')


# 5. Based on user input, display Name of student, Marks of student, his/her mean,median and rank

Slist.sort()
# Sort the Class by defining the __lt__ of sort() for the class so that the list is rankwise
# i+1 == rank
index=-1
for i in range(0,n):
    if(input==str(Slist[i].rollNo) or input==Slist[i].name):
        index=i
        break

if index==-1:
    print('INPUT NOT FOUND!!')
    exit()

print('Name: '+Slist[index].name)
print('RollNo: '+str(Slist[index].rollNo))
print('Total MARKS: '+str(Slist[index].total))
print('MATHS : '+str(Slist[index].maths))
print('CSE    :'+str(Slist[i].cse))
print('SCIENCE:'+str(Slist[i].science))
print('MEAN   :'+str(Slist[i].mean))
print('MEDIAN :'+str(Slist[index].median))
print('RANK   :'+str(index+1))
