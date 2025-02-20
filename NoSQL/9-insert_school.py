#!/usr/bin/env python3
'''
Write a Python function that inserts a new document in a collection based on kwargs:
'''
import pymongo


def insert_school(mongo_collection, **kwargs):
    '''
    Function inserts a new document in a collection
    based on kwargs and returns the new _id
    '''
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
