#!/usr/bin/env python3
"""
This module defines a Cache class that
uses Redis for storing and retrieving data.
"""

import redis
import uuid
from typing import Union


class Cache:
    """
    A class to represent a cache using Redis.

    Attributes
    ----------
    _redis : redis.Redis
        an instance of the Redis client
    """

    def __init__(self) -> None:
        """
        Initialize the Cache class by creating a Redis client instance
        and flushing the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in the Redis cache and return a unique key.

        Parameters
        ----------
        data : Union[str, bytes, int, float]
            The data to be stored in the cache.

        Returns
        -------
        str
            The unique key associated with the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
