#!/usr/bin/python3
"""
Module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity class

    Attributes:
        name(str): amenity name

    """
    name = ""
