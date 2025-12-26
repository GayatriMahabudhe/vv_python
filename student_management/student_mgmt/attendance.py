
"""Attendance management module."""
from . import datastore
from datetime import datetime

def mark_attendance(student_id: str, present: bool):
    record = {'timestamp': datetime.now(), 'present': present}
    if student_id not in datastore.attendance:
        datastore.attendance[student_id] = []
    datastore.attendance[student_id].append(record)

def attendance_percentage(student_id: str) -> float:
    records = datastore.attendance.get(student_id, [])
    if not records:
        return 0.0
    present_days = sum(1 for r in records if r['present'])
    return (present_days / len(records)) * 100
