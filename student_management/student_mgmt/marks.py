
"""Marks processing module (separate)."""
from . import datastore
import math

def add_marks(student_id: str, subject: str, marks: int):
    if student_id not in datastore.marks:
        datastore.marks[student_id] = {}
    datastore.marks[student_id][subject] = marks

def total_marks(student_id: str) -> int:
    subjects = datastore.marks.get(student_id, {})
    return sum(subjects.values())

def percentage(student_id: str) -> float:
    subjects = datastore.marks.get(student_id, {})
    if not subjects:
        return 0.0
    return (sum(subjects.values()) / (len(subjects) * 100)) * 100

def compute_grade(student_id: str) -> str:
    pct = percentage(student_id)
    rounded = math.ceil(pct)
    if rounded >= 90: return 'A+'
    elif rounded >= 80: return 'A'
    elif rounded >= 70: return 'B'
    elif rounded >= 60: return 'C'
    elif rounded >= 50: return 'D'
    else: return 'F'
