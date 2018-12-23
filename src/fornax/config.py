# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 16:02:07 2018

@author: Jedidiah Yohan
"""


class iConfig(object):

    def __init__(self, id: str):
        self.id = id

    @property
    def Id(self):
        return self.name

    @Id.setter
    def Id(self, name):
        self.name = name

    def __set__(self, table: dict):
        pass


class BotConfig(iConfig):

    def __init__(self, id: str):
        super().__init__(id)

    def __set__(self, table: dict):
        super().__set__(table)
