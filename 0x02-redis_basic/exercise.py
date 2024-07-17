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

    def get(
        self,
        key: str,
        fn: Optional[Callable[[bytes], Union[str, int, float, bytes]]] = None,
    ) -> Optional[Union[str, int, float, bytes]]:
        """
        Retrieve data from the Redis cache using the key and optionally
        convert it using the provided callable.

        Parameters
        ----------
        key : str
            The key associated with the data to retrieve.
        fn : Optional[Callable[[bytes], Union[str, int, float, bytes]]]
            A callable to convert the data to the desired format.

        Returns
        -------
        Optional[Union[str, int, float, bytes]]
            The data retrieved from the cache, optionally converted.
            Returns None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data from the Redis cache as a string.

        Parameters
        ----------
        key : str
            The key associated with the data to retrieve.

        Returns
        -------
        Optional[str]
            The data retrieved from the cache as a string.
            Returns None if the key does not exist.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data from the Redis cache as an integer.

        Parameters
        ----------
        key : str
            The key associated with the data to retrieve.

        Returns
        -------
        Optional[int]
            The data retrieved from the cache as an integer.
            Returns None if the key does not exist.
        """
        return self.get(key, fn=int)
