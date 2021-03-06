"""
    @File :   db_queries.py
    @Author : mukul
    @Date :   01-01-2022
"""
from database_connection import DBConnection
from models import EmployeePayroll

connection = DBConnection.establish_connection()
cursor = connection.cursor(buffered=True, dictionary=True)


def retrieve_one_employee(id: int):
    """
        desc: query to get a employee detail from database
        param: employee id
        return: employee detail in dictionary format
    """
    show_data_query = f"SELECT * FROM employee_details WHERE Id={id}"
    cursor.execute(show_data_query)
    employee = [i for i in cursor]
    if employee:
        return employee
    else:
        raise Exception("Employee with this Id doesn't exist!")


def retrieve_all_employees():
    """
        desc: query to get a employees detail from database
        return: list of all employees detail in dictionary format
    """
    show_data_query = "select * from employee_details"
    cursor.execute(show_data_query)
    employees = [i for i in cursor]
    if employees:
        return employees
    else:
        raise Exception("DB doesn't contain any employee data!")


def add_employee(emp: EmployeePayroll):
    """
        desc: query to insert employee details in database
        param: name, profile, gender, department, salary, start date.
        return: employee detail in dictionary format
    """
    show_data_query = "insert into employee_details (Id, Name, ProfileImage, Gender, Department, Salary, StartDate, " \
                      "Notes) values(%d,'%s', '%s', '%s', '%s', %0.2f, '%s', '%s')" \
                      % (emp.id, emp.name, emp.profile, emp.gender, emp.department, emp.salary, emp.start_date, emp.notes)
    cursor.execute(show_data_query)
    connection.commit()
    return emp


def delete_employee(id: int):
    """
        desc: query to delete employee details from database
        param: id: employee id, which you want to delete.
        return: employee id which is deleted from db
    """
    try:
        show_data_query = "delete from employee_details where Id = '%s'" % id
        cursor.execute(show_data_query)
        connection.commit()
        return id
    except Exception as e:
        return "Employee Id doesn't exist in database!!"


def update_employee(id: int, emp: EmployeePayroll):
    """
        desc: query to update employee details in database
        param: id, name, profile, gender, department, salary, start date.
        return: employee detail in dictionary format
    """
    try:
        show_data_query = "update employee_details set Name = '%s', ProfileImage = '%s', Gender = '%s', " \
                          "Department = '%s', Salary = '%0.2f', StartDate = '%s', Notes = '%s' where Id = %d" % \
                          (emp.name, emp.profile, emp.gender, emp.department, emp.salary, emp.start_date, emp.notes, id)
        cursor.execute(show_data_query)
        connection.commit()
        emp_data = retrieve_one_employee(id)
        return emp_data
    except Exception as e:
        return "Employee Id doesn't exist in database!!"

