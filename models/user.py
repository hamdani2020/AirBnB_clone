#!/usr/bin/python3
"""User Module"""

from models.base_model import BaseModel

class User(BaseModel):
    """Instantion of public class attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
