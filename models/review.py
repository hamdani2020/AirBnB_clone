#!/usr/bin/python3
""" For the Review Module"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Instantiation of review class"""
    place_id = ""
    user_id = ""
    text = ""
