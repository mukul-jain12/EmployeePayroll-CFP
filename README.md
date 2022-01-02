**#Employee Payroll Service (FastAPI - MySQL Without ORM)**

>installation process

pip install fastapi

pip install uvicorn

pip install mysql-connector-python

>APIs

1. @app.get("/employee/{id}") : This API get the details of an employee from database.
2. @app.get("/employee/") : This API get the details of all the employees from database.
3. @app.post("/add_employee/") : This API adds the new employee to the database table.
4. @app.delete("/delete_employee/{id}") : This API used to delete the employee detail from database.
5. @app.put("/update_employee/{id}") : This API used to update the employee details.
6. @app.get("/") : Home Page.


>Folder Structure

```
EmployeePayrollMgmt
├── myenv
├── .env
├── .gitignore
├── database_connection.py
├── db_queries.py
├── employee_payroll.log
├── main.py
├── models.py
├── requirement.txt
└── README.md
```