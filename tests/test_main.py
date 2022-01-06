import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestCase:

    def test_hello_world(self):
        """
        decs: test case for home page
        """
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome To FastAPI CRUD Operations"}

    @pytest.mark.parametrize('emp_id, emp_data',
                             [
                                 (2, [{"Id": 2, "Name": "Kachra Seth", "ProfileImage": "image3", "Gender": "Female",
                                       "Department": "HR", "Salary": 15000, "StartDate": "2018-12-24",
                                       "Notes": "Kabadi wala"}]),
                                 (6, [{"Id": 6, "Name": "Baburao Ganpatrao Apte", "ProfileImage": "image3",
                                       "Gender": "Male", "Department": "Finance", "Salary": 30000,
                                       "StartDate": "2016-12-24", "Notes": "Jai Maharashtra"}])
                             ])
    def test_retrieve_employee_detail_for_existing_id(self, emp_id, emp_data):
        """
        desc: test case for retrieval of an employee from database.
        param1: emp_id: it is an employee id
        param2: emp_data: all employee details
        """
        response = client.get(f"/employee/{emp_id}")
        assert response.status_code == 200
        assert response.json() == {"status": 200, "message": "Successfully Get The Employee Details", "data": emp_data}

    @pytest.mark.parametrize('emp_id', [12, 54, 23])
    def test_retrieve_employee_detail_for_non_existing_id(self, emp_id):
        """
        desc: test case for retrieval of an employee from database, but id doesn't exist, so it will raise exception
        """
        response = client.get(f"/employee/{emp_id}")
        # assert response.status_code == 404
        assert response.json() == {"status": 404, "message": "Error : Employee with this Id doesn't exist!"}

    def test_not_retrieving_all_employee_detail(self):
        """
        desc: test case for retrieving all employees, but raise exception if there is no data in db
        """
        response = client.get(f"/employees/")
        # assert response.status_code == 404
        assert response.json() == {"status": 404, "message": f"Error : DB doesn't contain any employee data!"}

    def test_retrieve_all_employee_detail(self):
        """
        desc: test case for retrieving all employees from database
        """
        response = client.get(f"/employees/")
        assert response.status_code == 200
        assert response.json() == {"status": 200, "message": "Successfully Get All Employee Details", "data": [
            {"Id": 1, "Name": "Mukul Jain", "ProfileImage": "image1", "Gender": "Male", "Department": "HR",
             "Salary": 85000, "StartDate": "2022-01-02", "Notes": "Sincere and Intelligent"},
            {"Id": 2, "Name": "Kachra Seth", "ProfileImage": "image3", "Gender": "Female", "Department": "HR",
             "Salary": 15000, "StartDate": "2018-12-24", "Notes": "Kabadi wala"},
            {"Id": 3, "Name": "Shivam Mishra", "ProfileImage": "image3", "Gender": "Male", "Department": "Finance",
             "Salary": 90000, "StartDate": "2021-12-22", "Notes": "Sincere and Intelligent"},
            {"Id": 4, "Name": "Raju", "ProfileImage": "image4", "Gender": "Male", "Department": "Other",
             "Salary": 1000, "StartDate": "2021-12-24", "Notes": "Topibaaz"},
            {"Id": 5, "Name": "Shyaam", "ProfileImage": "image3", "Gender": "Male", "Department": "HR",
             "Salary": 35000, "StartDate": "2018-12-24", "Notes": "Dupe"},
            {"Id": 6, "Name": "Baburao Ganpatrao Apte", "ProfileImage": "image3", "Gender": "Male",
             "Department": "Finance", "Salary": 30000, "StartDate": "2016-12-24", "Notes": "Jai Maharashtra"},
            {"Id": 19, "Name": "Mukul", "ProfileImage": "Tring", "Gender": "Male", "Department": "HR",
             "Salary": 50000000.2, "StartDate": "2022-01-05", "Notes": "string"},
            {"Id": 20, "Name": "alsjcn", "ProfileImage": "string", "Gender": "string", "Department": "string",
             "Salary": 0, "StartDate": "2022-01-05", "Notes": "string"}
        ]}

    def test_delete_employee_not_exist_in_db(self):
        """
        desc: test case for deleting employee, but id doesn't exist so it will raise exception
        """
        response = client.delete("/employee/22")
        assert response.json() == {"status": 404, "message": "Error : Employee with this Id doesn't exist!"}

    def test_delete_employee(self):
        """
        desc: test case for deleting employee, which send positive response
        """
        response = client.delete("/employee/20")
        assert response.json() == {"status": 200, "message": "Successfully Deleted The Employee Details", "data": 20}

    def test_add_employee(self):
        """
        desc: test case for add employee in database
        """
        response = client.post("/employee/", json={"id": 21, "name": "string", "profile": "string", "gender": "string",
                                                   "department": "string", "salary": 0, "start_date": "2022-01-06",
                                                   "notes": "string"})
        assert response.json() == {"status": 200, "message": "Successfully Get All Employee Details",
                                   "data": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMX0.Ol"
                                           "-y8_Of90PB2atTqmf9plt_PJV1t7vFKslyqYdAXOA"}

    def test_cannot_add_employee(self):
        """
        desc: test case for add employee, but raise exception if employee detail is already in db
        """
        response = client.post("/employee/", json={"id": 21, "name": "string", "profile": "string", "gender": "string",
                                                   "department": "string", "salary": 0, "start_date": "2022-01-06",
                                                   "notes": "string"})
        assert response.json() == {"status": 402, "message": "Error : Employee with this Id Already exist in database"}
