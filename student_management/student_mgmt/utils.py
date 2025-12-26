
"""Reusable utilities used across student applications."""
import random
import string

def generate_student_id(prefix: str = "STD") -> str:
    suffix = ''.join(random.choices(string.digits, k=5))
    return f"{prefix}{suffix}"

def validate_positive_int(value: int, field_name: str):
    if not isinstance(value, int) or value < 0:
        raise ValueError(f"{field_name} must be a non-negative integer")

def format_currency(amount: float) -> str:
    return f"₹{amount:,.2f}"
