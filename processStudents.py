''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv
from multiprocessing.dummy import Value

from numpy import append


# create a file object to open the file in read mode
students = open("students.csv", 'r')


# create a csv object from the file object
reader = csv.reader(students, delimiter = ',')

#skip the header row
next(students)

#create an outfile object for the pocessed record
outfile = open('processedStudents.csv', 'w')


#create a new dictionary named 'student_dict'
student_dict = {'Student_ID': []}


#use a loop to iterate through each row of the file
    #check if the GPA is below 3.0. If so, write the record to the outfile
for row in reader:
    if float(row[8]) < 3.0:
        outfile.write(str(row) + '\n')
        
      



    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
students = open('students.csv', 'r')
processed_reader = csv.reader(students, delimiter = ',')
next(processed_reader)
for row in processed_reader:
    student_dict['Student_ID'].append(row[0])

    
    





#print the entire dictionary
print(student_dict)

#Print the student id 
print(student_dict[5])

#print out the corresponding GPA from the dictionary
print(student_dict)


#close the outfile
outfile.close()







