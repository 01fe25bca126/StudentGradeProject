name = input("Enter Student Name: ")
department = input("Enter Department: ")
semester = input("Enter Semester: ")
m1 = float(input("Enter Marks in Subject 1: "))
m2 = float(input("Enter Marks in Subject 2: "))
m3 = float(input("Enter Marks in Subject 3: "))
average = (m1 + m2 + m3) / 3
if average >= 90:
    grade = "S"
elif average >= 80:
    grade = "A"
elif average >= 65:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"
print("----- Result -----")
print("Name:", name)
print("Department:", department)
print("Semester:", semester)
print("Average:", average)
print("Grade:", grade)