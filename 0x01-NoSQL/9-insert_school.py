#!/usr/bin/env python3

"""
lists all documents in a collection based
on kwargs
"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """Function to insert new document"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
