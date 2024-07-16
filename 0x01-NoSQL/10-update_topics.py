#!/usr/bin/env python3

"""This module provides functions 
for updating documents in MongoDB collections
"""

from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """update school topics based on the name"""
    result = mongo_collection.update_one(
        {"name": name},  # Filter to find the document by name
        {"$set": {"topics": topics}}  # Update the "topics" field
    )
    return result
