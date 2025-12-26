
"""Student data management module (user-defined)."""
from . import datastore

def add_student(student_id: str, name: str, batch: str, course: str) -> None:
    datastore.students[student_id] = {
        'id': student_id,
        'name': name,
        'batch': batch,
        'course': course
    }

def get_student(student_id: str):
    return datastore.students.get(student_id)

def update_student(student_id: str, **updates):
    if student_id not in datastore.students:
        raise KeyError(f"Student {student_id} not found")
    datastore.students[student_id].update(updates)

def delete_student(student_id: str):
    datastore.students.pop(student_id, None)

def list_students():
    return datastore.students
