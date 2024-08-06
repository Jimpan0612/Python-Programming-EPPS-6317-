"""Student gradebook
Program to track student frades

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

#Create list of students
student = []


while menu != 7:
    menu = int(input("Enter selection [1-7]"))

    if menu == 1:
        #Print column headers
        print("Name\tGrade")
        #Loop though stundents
        for s in student:
            print(s[0] + "\t" + str(s[1]))
        
    elif menu == 2:
        #Prompt user for student name
        sname = input("Student name? ")
        #Prompt user for student grade
        sgrade = input("Student grade? ")
        #Append student information to the list(list of name, grade)
        student.append([sname, sgrade])
        
    elif menu == 3:
        print(menu)
    elif menu == 4:
        print(menu)
    elif menu == 5:
        print(menu)
    elif menu == 6:
        print(menu)

print("Terminating program... Goodbye!")
