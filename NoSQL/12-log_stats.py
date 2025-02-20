#!/usr/bin/env python3
'''
Write a Python script that provides some stats
about Nginx logs stored in MongoDB:
'''
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{collection.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        method_docs = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_docs}")

    status = collection.count_documents({
        "$and": [
            {"method": "GET"},
            {"path": "/status"}
        ]
    })

    print(f"(status) status check")
