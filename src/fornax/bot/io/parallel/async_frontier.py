# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""
import sys


__all__ = ['AsyncFrontier']

from multiprocessing import Manager, Lock
from fornax.util.text.similarity.levenshtein import LevenshteinEdit


class AsyncFrontier(object):
    """

    """

    def __init__(self, seed: str, threshold=0.5):

        man = Manager()

        self.__lock = Lock()
        self.__seed = man.Value('u', seed)
        self.__flag = man.Value('f', threshold)
        self.__queue = man.dict()
        self.__edit = LevenshteinEdit()

    def __str__(self) -> str:
        return str(self.__queue.keys())

    def __score__(self, url: str) -> float:
        """

        :param url:
        :return:
        """
        return self.__edit.getDstance(self.__seed.value, url)

    def push(self, url: str):
        """

        :param url:
        :return:
        """
        if url not in self.__queue:
            sc = self.__score__(url)
            if sc > self.__flag.value:
                self.__queue[url] = sc

    def pop(self) -> str:
        try:
            m, item = 0.0, self.__queue.keys()[0]
            for i in self.__queue:
                if self.__queue[i] > m:
                    m = self.__queue[i]
                    item = i
                del self.__queue[item]
                return item
        except IndexError as ie:
            sys.stderr.write(str(ie))
            exit()

    def peek(self) -> str:
        return self.__queue.keys()[-1]

    def get(self, url) -> float or None:
        """

        :rtype: float or None
        :param url: 
        :return: 
        """
        try:
            return self.__queue[url]
        except KeyError:
            return None

    def update(self, url: str, score: float):
        """

        :param url: 
        :param score: 
        """
        self.__queue[url] = score

    def isempty(self) -> bool:
        return self.Size == 0

    @property
    def Size(self) -> int:
        return len(self.__queue)

    @property
    def Threshold(self) -> float:
        return self.__flag

    @Threshold.setter
    def Threshold(self, nthr: float):
        with self.__lock:
            self.__flag.value: float = nthr

    @property
    def Seed(self):
        return self.__seed

    @Seed.setter
    def Seed(self, seed: str):
        with self.__lock:
            self.__seed.value = seed
