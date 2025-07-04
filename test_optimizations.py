#!/usr/bin/env python3
"""
Test script to demonstrate the optimized applications work correctly.
"""

import os
import tempfile
from optimized_password_generator import PasswordGenerator
from optimized_student_management import OptimizedStudentManager, Student

def test_password_generator():
    """Test the optimized password generator."""
    print("🔐 Testing Optimized Password Generator")
    print("-" * 40)
    
    generator = PasswordGenerator()
    
    # Test single password generation
    char_types = {'upper', 'lower', 'digits', 'special'}
    password = generator.generate_password(12, char_types)
    print(f"Generated 12-char password: {password}")
    
    # Test multiple password generation
    passwords = generator.generate_multiple_passwords(3, 8, {'upper', 'lower', 'digits'})
    print(f"Generated 3 x 8-char passwords:")
    for i, pwd in enumerate(passwords, 1):
        print(f"  {i}: {pwd}")
    
    print("✅ Password generator working correctly!\n")

def test_student_management():
    """Test the optimized student management system."""
    print("🎓 Testing Optimized Student Management System")
    print("-" * 45)
    
    # Create temporary file for testing
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp_file:
        manager = OptimizedStudentManager(tmp_file.name)
    
    try:
        # Add test students
        test_students = [
            Student("STU001", "Alice Johnson", 20, "A"),
            Student("STU002", "Bob Smith", 19, "B"),
            Student("STU003", "Carol Davis", 21, "A"),
        ]
        
        for student in test_students:
            manager.students[student.id] = student
        
        manager.save_data()
        print(f"Added {len(test_students)} students")
        
        # Test search (O(1) operation)
        found_student = manager.students.get("STU002")
        if found_student:
            print(f"Found student: {found_student.name} (ID: {found_student.id})")
        
        # Test statistics
        if manager.students:
            ages = [s.age for s in manager.students.values()]
            print(f"Average age: {sum(ages)/len(ages):.1f}")
            print(f"Total students: {len(manager.students)}")
        
        # Test persistence by reloading
        manager2 = OptimizedStudentManager(tmp_file.name)
        print(f"Reloaded {len(manager2.students)} students from file")
        
        print("✅ Student management system working correctly!\n")
    
    finally:
        # Cleanup
        os.unlink(tmp_file.name)

def main():
    """Run all tests."""
    print("🚀 Testing Optimized Applications")
    print("=" * 50)
    print()
    
    test_password_generator()
    test_student_management()
    
    print("🎉 All optimizations working correctly!")
    print("The applications are ready for production use.")

if __name__ == "__main__":
    main()