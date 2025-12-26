
"""Fee management module."""
from . import datastore
from .utils import format_currency

_fee_structure = {'base_fee': 0, 'scholarship_percent': 0}

def set_fee_structure(base_fee: int, scholarship_percent: int = 0):
    _fee_structure['base_fee'] = base_fee
    _fee_structure['scholarship_percent'] = scholarship_percent

def fee_due(student_id: str) -> float:
    base = _fee_structure['base_fee']
    disc = base * (_fee_structure['scholarship_percent'] / 100.0)
    due = base - disc
    paid = sum(p['amount'] for p in datastore.fees.get(student_id, []))
    return max(due - paid, 0.0)

def record_payment(student_id: str, amount: int):
    if student_id not in datastore.fees:
        datastore.fees[student_id] = []
    datastore.fees[student_id].append({'amount': amount})

def fee_summary(student_id: str) -> str:
    return f"Outstanding: {format_currency(fee_due(student_id))}"
