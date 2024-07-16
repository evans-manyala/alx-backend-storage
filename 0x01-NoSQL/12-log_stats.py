#!/usr/bin/env python3
"""This module provides functions to
analyze Nginx logs in a MongoDB database.
"""

from pymongo import MongoClient


def get_stats():
    """"
    Provides statistics about Nginx logs
    in a MongoDB collection.
    """
    client = MongoClient('mongodb://localhost:27017')
    nginx = client.logs.nginx
    print(f"{nginx.count_documents({})} logs")
    print("Methods:")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = nginx.count_documents({'method': method})
        print(f"\tmethod {method}: {count}")
    get_count = nginx.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{get_count} status check")


if __name__ == "__main__":
    get_stats()
