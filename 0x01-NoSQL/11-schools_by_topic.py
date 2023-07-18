#!/usr/bin/env python3
"""This module contains a function that interacts with a mongo database"""


def schools_by_topic(mongo_collection, topic):
    """This function returns a list of schools that have a specified topic"""
    return mongo_collection.find({'topics': {'$elemMatch': {'$eq': topic}}})
