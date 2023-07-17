#!/usr/bin/env python3
"""This module contains a function that interacts with a mongodb"""


def insert_school(mongo_collection, **kwargs):
    """This function inserts a document into a collection"""
    return mongo_collection.insert_one(kwargs).inserted_id
