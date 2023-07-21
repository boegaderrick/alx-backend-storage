#!/usr/bin/env python3
"""
    This module contains a function that sends a get request and
    a decorator function that keeps count of the number of get
    requests made. The results of the get requests are also cached
    and prioritized for return if the TTL has not run out.
"""
from functools import wraps
from redis import Redis
from requests import get
from typing import Any, Callable

redis: Redis = Redis()


def counter(function: Callable) -> Callable:
    """
        This function keeps track of number of requests to a url
        Every time a get request is sent the results are also cached
    """
    @wraps(function)
    def inner(url: str) -> str:
        """This function handles the counting in the database"""
        cacheName: str = 'cache:' + url
        page: Any
        if redis.ttl(cacheName) < 1:
            page = function(url)
            redis.setex(cacheName, 10, page)

            urlCount: str = 'count:' + url
            redis.incr(urlCount)
            redis.setex(cacheName, 10, page)
        else:
            page = redis.get(cacheName)
            page = page.decode()

        return page
    return inner


@counter
def get_page(url: str) -> str:
    """This function sends a get request to a url"""
    page = get(url)
    return page.text
