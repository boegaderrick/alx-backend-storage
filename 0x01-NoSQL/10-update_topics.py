#!/usr/bin/env python3
"""This module contains a function that interacts with a mongodb"""


def update_topics(mongo_collection, name, topics):
    """This function updates a mongodb collection"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
