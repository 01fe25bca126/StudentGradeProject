def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def calculate_average(marks):
    return sum(marks) / len(marks)

if __name__ == "__main__":
    try:
        name = input("Enter Student Name: ")
        m1 = int(input("Enter Marks 1: "))
        m2 = int(input("Enter Marks 2: "))
        m3 = int(input("Enter Marks 3: "))
    except EOFError:
        print("Running in Jenkins - Using Default Values")
        name = "Neha"
        m1 = 85
        m2 = 90
        m3 = 95

    marks = [m1, m2, m3]
    avg = calculate_average(marks)
    grade = calculate_grade(avg)

    print(f"Student: {name}")
    print(f"Average: {avg}")
    print(f"Grade: {grade}")