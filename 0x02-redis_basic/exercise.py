#!/usr/bin/env python3
"""This module contains Cache class"""
from redis import Redis
from typing import Union
from uuid import uuid4


class Cache:
    """Cache class definition"""
    _redis: Redis

    def __init__(self):
        """Cache class object instantiation"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This method sets a key-value pair in the database"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
