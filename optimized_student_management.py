import json
import os
from typing import Dict, Optional
from dataclasses import dataclass, asdict

@dataclass
class Student:
    """Student data class with validation."""
    id: str
    name: str
    age: int
    grade: str
    
    def __post_init__(self):
        """Validate student data after initialization."""
        if not self.id.strip():
            raise ValueError("Student ID cannot be empty")
        if not self.name.strip():
            raise ValueError("Student name cannot be empty")
        if self.age < 0 or self.age > 150:
            raise ValueError("Age must be between 0 and 150")
        if not self.grade.strip():
            raise ValueError("Grade cannot be empty")

class OptimizedStudentManager:
    """
    Optimized Student Management System with O(1) lookups and data persistence.
    """
    
    def __init__(self, data_file: str = "students.json"):
        # Use dictionary for O(1) lookups instead of list with O(n) search
        self.students: Dict[str, Student] = {}
        self.data_file = data_file
        self.load_data()
    
    def load_data(self):
        """Load student data from file if exists."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    for student_data in data:
                        student = Student(**student_data)
                        self.students[student.id] = student
                print(f"Loaded {len(self.students)} students from {self.data_file}")
            except (json.JSONDecodeError, TypeError, ValueError) as e:
                print(f"Error loading data: {e}")
    
    def save_data(self):
        """Save student data to file."""
        try:
            with open(self.data_file, 'w') as f:
                student_list = [asdict(student) for student in self.students.values()]
                json.dump(student_list, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_student(self) -> bool:
        """Add a new student with validation."""
        try:
            student_id = input("Enter Student ID: ").strip()
            
            # Check for duplicate ID - O(1) operation
            if student_id in self.students:
                print("Error: Student ID already exists!")
                return False
            
            name = input("Enter Name: ").strip()
            age = int(input("Enter Age: "))
            grade = input("Enter Grade: ").strip()
            
            student = Student(student_id, name, age, grade)
            self.students[student_id] = student  # O(1) insertion
            self.save_data()
            print("Student added successfully!\n")
            return True
            
        except ValueError as e:
            print(f"Error: {e}\n")
            return False
    
    def view_students(self):
        """View all students with efficient iteration."""
        if not self.students:
            print("No students found.\n")
            return
        
        print(f"\n--- Student List ({len(self.students)} students) ---")
        # Sort by ID for consistent output
        for student_id in sorted(self.students.keys()):
            student = self.students[student_id]
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
        print()
    
    def search_student(self) -> Optional[Student]:
        """Search for a student - O(1) operation."""
        student_id = input("Enter Student ID to search: ").strip()
        
        student = self.students.get(student_id)  # O(1) lookup
        if student:
            print(f"Found: ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}\n")
            return student
        else:
            print("Student not found.\n")
            return None
    
    def update_student(self) -> bool:
        """Update student information - O(1) operation."""
        student_id = input("Enter Student ID to update: ").strip()
        
        if student_id not in self.students:  # O(1) check
            print("Student not found.\n")
            return False
        
        try:
            current_student = self.students[student_id]
            print(f"Current data: Name: {current_student.name}, Age: {current_student.age}, Grade: {current_student.grade}")
            
            name = input("Enter new Name (or press Enter to keep current): ").strip()
            age_input = input("Enter new Age (or press Enter to keep current): ").strip()
            grade = input("Enter new Grade (or press Enter to keep current): ").strip()
            
            # Update only if new values provided
            if name:
                current_student.name = name
            if age_input:
                current_student.age = int(age_input)
            if grade:
                current_student.grade = grade
            
            # Validate updated student
            Student(current_student.id, current_student.name, current_student.age, current_student.grade)
            
            self.save_data()
            print("Student updated successfully!\n")
            return True
            
        except ValueError as e:
            print(f"Error: {e}\n")
            return False
    
    def delete_student(self) -> bool:
        """Delete a student - O(1) operation."""
        student_id = input("Enter Student ID to delete: ").strip()
        
        if student_id in self.students:  # O(1) check
            student = self.students.pop(student_id)  # O(1) deletion
            self.save_data()
            print(f"Student {student.name} (ID: {student_id}) deleted successfully!\n")
            return True
        else:
            print("Student not found.\n")
            return False
    
    def get_statistics(self):
        """Display statistics about the student database."""
        if not self.students:
            print("No students in database.\n")
            return
        
        ages = [student.age for student in self.students.values()]
        grades = [student.grade for student in self.students.values()]
        
        print(f"\n--- Database Statistics ---")
        print(f"Total students: {len(self.students)}")
        print(f"Average age: {sum(ages) / len(ages):.1f}")
        print(f"Age range: {min(ages)} - {max(ages)}")
        
        # Grade distribution
        grade_count = {}
        for grade in grades:
            grade_count[grade] = grade_count.get(grade, 0) + 1
        
        print("Grade distribution:")
        for grade, count in sorted(grade_count.items()):
            print(f"  {grade}: {count} students")
        print()

def main():
    """Main program with enhanced menu system."""
    manager = OptimizedStudentManager()
    
    while True:
        print("====== Optimized Student Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Statistics")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        try:
            if choice == "1":
                manager.add_student()
            elif choice == "2":
                manager.view_students()
            elif choice == "3":
                manager.search_student()
            elif choice == "4":
                manager.update_student()
            elif choice == "5":
                manager.delete_student()
            elif choice == "6":
                manager.get_statistics()
            elif choice == "7":
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please try again.\n")
        
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}\n")

if __name__ == "__main__":
    main()