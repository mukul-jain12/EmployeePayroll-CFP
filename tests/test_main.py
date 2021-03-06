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
        json_response = response.json()
        assert json_response["message"] == "Error : Employee with this Id doesn't exist!"

    def test_not_retrieving_all_employee_detail(self):
        """
        desc: test case for retrieving all employees, but raise exception if there is no data in db
        """
        response = client.get(f"/employees/")
        # assert response.status_code == 404
        json_response = response.json()
        assert json_response["message"] == "Error : DB doesn't contain any employee data!"

    def test_retrieve_all_employee_detail(self):
        """
        desc: test case for retrieving all employees from database
        """
        response = client.get("/employees/")
        assert response.status_code == 200
        json_response = response.json()
        assert json_response["message"] == "Successfully Get All Employee Details"

    def test_delete_employee_not_exist_in_db(self):
        """
        desc: test case for deleting employee, but id doesn't exist, so it will raise exception
        """
        response = client.delete("/employee/22")
        json_response = response.json()
        assert json_response["message"] == "Error : Employee with this Id doesn't exist!"

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
        json_response = response.json()
        assert json_response[
                   "data"] == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMX0.Ol-y8_Of90PB2atTqmf9plt_PJV1t7vFKslyqYdAXOA"

    def test_cannot_add_employee(self):
        """
        desc: test case for add employee, but raise exception if employee detail is already in db
        """
        response = client.post("/employee/", json={"id": 21, "name": "string", "profile": "string", "gender": "string",
                                                   "department": "string", "salary": 0, "start_date": "2022-01-06",
                                                   "notes": "string"})
        json_response = response.json()
        assert json_response["message"] == "Error : Employee with this Id Already exist in database"

    def test_login_api(self):
        """
        desc: test case for login
        """
        response = client.post("/login/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMX0.Ol-y8_Of90PB2atTqmf9plt_PJV1t7vFKslyqYdAXOA"})
        json_response = response.json()
        assert json_response["message"] == "Successfully Logged In"

    def test_cannot_login(self):
        """
        desc: test case for add employee, but raise exception if employee detail is already in db
        """
        response = client.post("/login/", headers={
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyMX0.Ol-y8_Of90PB2atTqmf9plt_PJV1t7vFKslyqYdAXOA"})
        json_response = response.json()
        assert json_response["message"] == "You are not authorized employee"

    def test_update_employee(self):
        """
        desc: test case for add employee, but raise exception if employee detail is already in db
        """
        response = client.put("/employee/6",
                              json={"id": 6, "name": "Baburao Ganpatrao Apte", "profile": "image4", "gender": "Male",
                                    "department": "Finance", "salary": 30000, "start_date": "2016-12-24",
                                    "notes": "Jai Maharashtra"})
        json_response = response.json()
        assert json_response["message"] == "Successfully Updated The Employee Details"

    def test_not_update_employee(self):
        """
        desc: test case for add employee, but raise exception if employee detail is already in db
        """
        response = client.put("/employee/18",
                              json={"id": 18, "name": "Baburao Ganpatrao Apte", "profile": "image4", "gender": "Male",
                                    "department": "Finance", "salary": 30000, "start_date": "2016-12-24",
                                    "notes": "Jai Maharashtra"})
        json_response = response.json()
        assert json_response["message"] == "Error : Employee with this Id doesn't exist!"
