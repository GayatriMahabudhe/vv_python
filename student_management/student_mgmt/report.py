
"""Report generation module using classes, connected to main student system."""
from .student import get_student
from .marks import total_marks, percentage, compute_grade
from .attendance import attendance_percentage
from .fees import fee_summary

class BaseReport:
    def __init__(self, title: str = "Report"):
        self.title = title
    def header(self) -> str:
        return f"""
--- {self.title} ---
"""

class StudentReport(BaseReport):
    def __init__(self, student_id: str):
        super().__init__(title=f"Student Report ({student_id})")
        self.student_id = student_id

    def build_summary(self) -> str:
        s = get_student(self.student_id)
        if not s:
            return self.header() + "Student not found."
        tm = total_marks(self.student_id)
        pct = percentage(self.student_id)
        grade = compute_grade(self.student_id)
        att_pct = attendance_percentage(self.student_id)
        fee = fee_summary(self.student_id)

        return f"""{self.header()}
Name     : {s['name']}
Batch    : {s['batch']} | Course: {s['course']}
Marks    : Total={tm}, Percentage={pct:.2f}%, Grade={grade}
Attendance: {att_pct:.2f}%
Fees     : {fee}
"""
