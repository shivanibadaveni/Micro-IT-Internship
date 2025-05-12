students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")
    student = {"ID": student_id, "Name": name, "Age": age, "Grade": grade}
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}")
    print()

def search_student():
    student_id = input("Enter Student ID to search: ")
    for student in students:
        if student["ID"] == student_id:
            print(f"Found: ID: {student['ID']}, Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}\n")
            return
    print("Student not found.\n")

def update_student():
    student_id = input("Enter Student ID to update: ")
    for student in students:
        if student["ID"] == student_id:
            student["Name"] = input("Enter new Name: ")
            student["Age"] = input("Enter new Age: ")
            student["Grade"] = input("Enter new Grade: ")
            print("Student updated successfully!\n")
            return
    print("Student not found.\n")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    for student in students:
        if student["ID"] == student_id:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")

def menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")

menu()
