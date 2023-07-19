#!/usr/bin/env python3
"""This module contains Cache class"""
from redis import Redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache class definition"""
    __redis: Redis

    def __init__(self):
        """Cache class object instantiation"""
        self.__redis = Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This method sets a value to a key in the database"""
        key: str = str(uuid4())
        self.__redis.set(key, data)
        return key
