#!/usr/bin/env python3
"""This module contains a function that interacts with a mongodb"""


def list_all(mongo_collection):
    """This function lists all documents in a mongodb collection"""
    return mongo_collection.find()
