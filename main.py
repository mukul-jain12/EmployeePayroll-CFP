"""
    @File :   main.py
    @Author : mukul
    @Date :   01-01-2022
"""
import logging

import uvicorn
from fastapi import FastAPI, Header

from db_queries import *
from models import EmployeePayroll
from generate_token import *
app = FastAPI()

logging.basicConfig(filename='employee_payroll.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


@app.get("/")
def hello_world():
    logging.info("It's a Home Page")
    return {'message': 'Welcome To FastAPI CRUD Operations'}


@app.get("/employee/{id}")
def retrieve_employee_detail(id: int):
    """
    desc: created api to get only one item from the table
    param: employee id
    return: employee details in SMD format
    """
    try:
        employee_details = retrieve_one_employee(id)
        logging.info("Successfully Get Employee Details")
        logging.debug(f"Employee Details are : {employee_details}")
        return {"status": 200, "message": "Successfully Get The Employee Details", "data": employee_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.get("/employees/")
def retrieve_all_employee_details():
    """
    desc: created api to get all items from the table
    return: employee details in SMD format
    """
    try:
        employee_details = retrieve_all_employees()
        logging.info("Successfully Get All Employee Details")
        logging.debug(f"Employee Details are : {employee_details}")
        return {"status": 200, "message": "Successfully Get All Employee Details", "data": employee_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.post("/employee/")
def add_employee_details(emp: EmployeePayroll):
    """
    desc: created api to insert item in the database table
    param1: EmployeePayroll class which contains schema
    return: employee details in SMD format
    """
    try:
        employee_details = add_employee(emp)
        logging.info("Successfully Added Employee Details")
        logging.debug(f"Employee Details are : {employee_details}")
        token_id = encode_token(emp.id)
        return token_id
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.delete("/employee/{id}")
def delete_employee_details(id: int):
    """
    desc: created api to delete the items from the database table using id
    param: id: it is an employee id
    return: employee id in SMD format
    """
    try:
        retrieve_one_employee(id)
        emp_id = delete_employee(id)
        logging.info("Successfully Deleted The Employee Details")
        logging.debug(f"Employee ID is : {emp_id}")
        return {"status": 200, "message": "Successfully Deleted The Employee Details", "data": emp_id}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.put("/employee/{id}")
def update_employee_details(id: int, emp: EmployeePayroll):
    """
    desc: created api to update any item in the database table
    param1: id: it is an employee id
    param2: EmployeePayroll class which contains schema
    return: employee details in SMD format
    """
    try:
        retrieve_one_employee(id)
        employee_details = update_employee(id, emp)
        logging.info("Successfully Updated The Employee Details")
        logging.debug(f"Employee Details are : {employee_details}")
        return {"status": 200, "message": "Successfully Updated The Employee Details", "data": employee_details}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": f"Error : {e}"}


@app.post("/login/{id}")
def login(token: str = Header(None)):
    """
        desc: employee login by entering the token number generated at employee creation time
        param: token: encoded employee id
        return
    """
    try:
        token_id = decode_token(token)
        check_emp_in_db = retrieve_one_employee(token_id)
        return {"status": 200, "message": "Successfully Logged In", "data": check_emp_in_db}
    except Exception as e:
        logging.error(f"Error: {e}")
        return {"status": 500, "message": "You are not authorized employee"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)
