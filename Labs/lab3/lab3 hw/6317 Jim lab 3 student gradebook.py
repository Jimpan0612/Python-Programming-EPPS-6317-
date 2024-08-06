"""6317 Lab3 Student gradebook
Program to track student grades

References
-----------

"""

_auther_ = "Jim <cxp220025@utdallas.edu>"


menu = ""
print("What would you like to do?")
print("\t[1] Show full gradebook")
print("\t[2] Add Student")
print("\t[3] Remove Student")
print("\t[4] Modify Student Information")
print("\t[5] Display Highest Grade")
print("\t[6] Display Lowest Grade")
print("\t[7] Quit")

# Create list of students
student = []


while menu != 7:
    menu = int(input("Enter selection [1-7]"))

    if menu == 1:
        # Print column headers
        print("Name\tGrade")
        # Loop though stundents
        for s in student:
            print(s[0] + "\t" + str(s[1]))        
    elif menu == 2:
        # Prompt user for student name
        sname = input("Student name? ")
        # Prompt user for student grade
        sgrade = input("Student grade? ")
        # Append student information to the list(list of name, grade)
        student.append([sname, sgrade])       
    elif menu == 3:
        # Prompt user for student name to remove
        sname = input("Student to remove? ")
        found = False
        for s in student:
            if s[0] == sname:
                student.remove(s)
                print("The grade of {sname} is removed.")
                found = True
                break
        if not found:
            print("Student '{sname}' not found in the GradeBook. Unable to remove.")
    elif menu == 4:
        # Prompt user for student name to modify
        sname = input("Student to modify? ")
        found = False
        for s in student:
            if s[0] == sname:
                # Prompt user for modified name (default to original)
                new_name = input("Name: (press Enter to keep original value: {s[0]})")
                if new_name.strip() != "":
                    s[0] = new_name
                # Prompt user for modified grade (default to original)
                new_grade = input("Grade: (press Enter to keep original value: {s[1]})")
                if new_grade.strip() != "":
                    s[1] = new_grade
                print("Saved.")
                found = True
                break
        if not found:
            print(f"Student '{sname}' not found in the GradeBook. Unable to modify.")        
    elif menu == 5:
        if not student:
            print("No students in the GradeBook.")
        else:
            max_grade_student = max(student, key=lambda x: x[1])
            print(f"{max_grade_student[0]} had the highest score in the class: {max_grade_student[1]}")
    elif menu == 6:
        if not student:
            print("No students in the GradeBook.")
        else:
            min_grade_student = min(student, key=lambda x: x[1])
            print(f"{min_grade_student[0]} had the lowest score in the class: {min_grade_student[1]}")
    elif menu == 7:
        print("Exiting the program.")
    else:
        print("Invalid menu selection. Please enter a valid option (1-7).")

print("Terminating program... Goodbye!")
