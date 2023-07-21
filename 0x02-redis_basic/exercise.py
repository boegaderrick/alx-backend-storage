#!/usr/bin/env python3
"""This module contains Cache class"""
from functools import wraps
from typing import Any, Callable, List, Union
from uuid import uuid4
import redis


def replay(method: Callable) -> None:
    """This function prints the history of method calls"""
    qName = method.__qualname__
    red: redis.Redis = redis.Redis()
    count: Any = red.get(qName)
    inputs: List[bytes] = red.lrange(f'{qName}:inputs', 0, -1)
    outputs: List[bytes] = red.lrange(f'{qName}:outputs', 0, -1)

    print(f'{qName} was called {int(count)} times:')
    for inp, outp in zip(inputs, outputs):
        try:
            print(f"{qName}(*{int(inp)}) -> {outp.decode()}")
        except Exception:
            print(f"{qName}(*{inp.decode()}) -> {outp.decode()}")


def call_history(method: Callable) -> Callable:
    """This function keeps track of inputs and outputs of methods"""
    @wraps(method)
    def tracker(self, data: Union[str, bytes, int, float]) -> str:
        """This function updates the outputs and inputs lists"""
        output: str = method(self, data)
        self._redis.rpush(f'{method.__qualname__}:inputs', str((data,)))
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return tracker


def count_calls(method: Callable) -> Callable:
    """This function keeps track of how many times a method is called"""
    name: str = method.__qualname__
    @wraps(method)
    def counter(self, data: Union[str, bytes, int, float]) -> str:
        """This function handles the incrementation"""
        self._redis.incr(name)
        return method(self, data)
    return counter


class Cache:
    """Cache class definition"""
    _redis: redis.Redis

    def __init__(self) -> None:
        """Cache class object instantiation"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This method sets a key-value pair in the database"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Union[Callable, None] = None) -> Any:
        """Retrieves data and converts it to desired format using 'fn'"""
        value: Union[bytes, None] = self._redis.get(key)
        if value and fn:
            try:
                value = fn(value)
            except TypeError:
                pass
        return value

    def get_str(self, key: str) -> str:
        """This method gets string values from the database"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """This method gets int values from the database"""
        return self.get(key, int)
