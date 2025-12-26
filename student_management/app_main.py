
"""Main program that wires up all modules and demonstrates imports."""

# Different import styles
import student_mgmt.student as student                  # alias import for module
from student_mgmt.marks import add_marks, compute_grade # from ... import specific functions
import student_mgmt.report as rpt                       # alias for report module
from student_mgmt import attendance as att              # package-level import with alias
import student_mgmt.utils as utils                      # reusable utilities
import student_mgmt.fees as fees                        # regular import
from student_mgmt import demo_properties                # import a module to print properties
from student_mgmt import datastore                      # ✅ import datastore directly

def main():
    print()  # blank line
    print("=== Student Management System Demo ===")
    print()  # blank line

    # Create students (uses utils for ID generation)
    sid1 = utils.generate_student_id()
    sid2 = utils.generate_student_id()

    student.add_student(sid1, name="Aarav Sharma", batch="2025", course="CS")
    student.add_student(sid2, name="Isha Patil", batch="2025", course="IT")

    # Update a student
    student.update_student(sid2, course="CSE")

    # Marks processing (from ... import ...)
    add_marks(sid1, subject="Python", marks=88)
    add_marks(sid1, subject="Maths", marks=92)
    add_marks(sid2, subject="Python", marks=76)
    add_marks(sid2, subject="Maths", marks=81)

    # Attendance (alias import)
    att.mark_attendance(sid1, present=True)
    att.mark_attendance(sid1, present=False)
    att.mark_attendance(sid2, present=True)

    # Fees
    fees.set_fee_structure(base_fee=50000, scholarship_percent=10)
    fees.record_payment(sid1, amount=20000)
    fees.record_payment(sid2, amount=30000)

    # Generate reports using classes
    report = rpt.StudentReport(student_id=sid1)
    print(report.build_summary())

    report2 = rpt.StudentReport(student_id=sid2)
    print(report2.build_summary())

    # Demonstrate compute_grade
    print()  # blank line
    print("Computed Grade for {}: {}".format(sid1, compute_grade(sid1)))

    # Show module properties
    print()
    print("=== Module Properties Demo ===")
    demo_properties.print_module_properties()

    # List current data snapshot
    print()
    print("=== Data Snapshot ===")
    print("Students:")
    for sid, s in student.list_students().items():
        print(sid, s)

    print()
    print("Marks:")
    for sid, m in datastore.marks.items():
        print(sid, m)

    print()
    print("Attendance:")
    for sid, a in datastore.attendance.items():
        print(sid, a)

    print()
    print("Fees:")
    for sid, f in datastore.fees.items():
        print(sid, f)

if __name__ == '__main__':
    main()
