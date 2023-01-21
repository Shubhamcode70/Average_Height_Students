#Average Height of the Student
Student_height = input("Enter the value of heights separated by comma : ").split()
for n in range (0, len(Student_height)):
    Student_height[n] = int(Student_height[n])
print(Student_height)

#calculating sum of Student Heights
'''
total_height = sum(Student_Height)
total_height_input = len(student_height")
average_height = total_height / total_height_input
'''
#total_height calculation using for loop
total_height = 0
for height in Student_height:
    total_height += height
    #total_height = total_height + height
print(total_height)

#total_height_input calculation using for loop
total_students = 0
for studnets in Student_height:
    #total_students = total_student + 1
    total_students += 1
print(total_students)

#calculate the average height of the student and print it.
average_height = total_height / total_students
print(average_height)