# Function to determine the letter grade
def getLetterGrade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


# Input
studentName = input("Enter the student name: ")

grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))
grade4 = float(input("Enter grade 4: "))
grade5 = float(input("Enter grade 5: "))

# Store grades in a list
grades = [grade1, grade2, grade3, grade4, grade5]

# Calculate average
average = sum(grades) / len(grades)

# Output
print()
print(studentName)
print()
print("Average:", average)
print()
print("Letter Grade:", getLetterGrade(average))