#!/usr/bin/env python3
'''
Write a Python function that changes all topics of a school document based on the name:
'''
import pymongo


def update_topics(mongo_collection, name, topics):
    '''
    Function changes all topics of a school document
    based on the name
    '''
    return mongo_collection.update_many({
        "name": name
    }, {
        "$set": {
            "topics": topics
        }
    })
