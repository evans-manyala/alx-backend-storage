#!/usr/bin/env python3
"""This module provides functions to
analyze Nginx logs in a MongoDB database.
"""

from pymongo import MongoClient


def nginx_stats(mongo_collection):
    """
    Provides statistics about Nginx logs
    in a MongoDB collection.
    """
    total_logs = mongo_collection.count_documents()
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_logs = mongo_collection.count_documents
    ({"method": "GET", "path": "/status"})
    print(f"{status_logs} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
    nginx_collection = db["nginx"]

    nginx_stats(nginx_collection)
