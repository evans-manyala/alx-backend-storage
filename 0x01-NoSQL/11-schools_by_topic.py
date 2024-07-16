#!/usr/bin/env python3
"""
This module provides functions
for querying MongoDB collections.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a list of schools offering a specific topic.
    """

    schools = list(mongo_collection.find({"topics": topic}))
    return schools
