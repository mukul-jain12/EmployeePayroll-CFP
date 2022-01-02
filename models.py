"""
    @File :   models.py
    @Author : mukul
    @Date :   01-01-2022
"""
from datetime import date

from pydantic import BaseModel


class EmployeePayroll(BaseModel):
    id: int
    name: str
    profile: str
    gender: str
    department: str
    salary: float
    start_date: date
    notes: str
