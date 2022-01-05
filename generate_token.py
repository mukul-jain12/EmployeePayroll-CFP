"""
    @File :   generate_token.py
    @Author : mukul
    @Date :   05-01-2022
"""
import jwt


def encode_token(emp_id):
    """
        desc: this function will encode the payload into a token
        param: emp_id: it is an employee id
        return: generated token id
    """
    payload = {"user_id": emp_id}
    token_id = jwt.encode(payload, "secret")
    return token_id


def decode_token(token_id):
    """
        desc: this function will decode the token into a payload
        param: token_id: it is a token which generated at the time of adding an employee
        return: decoded employee id
    """
    payload = jwt.decode(token_id, "secret", algorithms=["HS256"])
    return payload.get('user_id')
