# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""

from multiprocessing import Process

from fornax.config import BotConfig
from io.parallel import AsyncFrontier


class AsyncBot(Process):

    def __int__(self, frontier: AsyncFrontier, conf: BotConfig):
        self.frontier = frontier
        self.config = conf
        pass
