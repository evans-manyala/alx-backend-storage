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

    client = MongoClient()
    logs = client.logs.nginx

    print(logs.count_documents({}), "logs")
    print("Methods:")

    for method in ("GET", "POST", "PUT", "PATCH", "DELETE"):
        print(
            f"\tmethod {method}: {logs.count_documents({'method': method})}"
            )

        print(
            f"{logs.count_documents({'path': '/status'})} status check"
            )


if __name__ == "__main__":
    nginx_stats()
