"""
    @File :   database_connection.py
    @Author : mukul
    @Date :   01-01-2022
"""
import logging
import os

from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv()

logging.basicConfig(filename='employee_payroll.log', filemode='a', level=logging.DEBUG,
                    format='%(levelname)s :: %(name)s :: %(asctime)s :: %(message)s')


class DBConnection:

    @staticmethod
    def establish_connection():
        """
            desc: Established database connection and perform query to created database
        """
        try:
            logging.info("Trying to establish the database connection")
            connection = connect(
                host=os.getenv('host'),
                user=os.getenv('user_name'),
                password=os.getenv('user_password'),
                database="employee_payroll_service",
            )
            logging.info("Database Connection is Established")
            return connection
        except Error as e:
            logging.error("Connection not Established")
            return {"status": 502, "message": "Error : Connection not Established"}
