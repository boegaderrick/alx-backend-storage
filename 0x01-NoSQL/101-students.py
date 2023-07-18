#!/usr/bin/env python3
"""This module contains a function that interacts with a database"""


def top_students(mongo_collection):
    """This function calculates the average score of all students"""
    pipeline = [
            {"$unwind": "$topics"},
            {"$group": {
                "_id": "$_id",
                "averageScore": {"$avg": "$topics.score"},
                "name": {"$first": "$name"}
                }
             },
            {"$sort": {"averageScore": -1}}
            ]
    return mongo_collection.aggregate(pipeline)
