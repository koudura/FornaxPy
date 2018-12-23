# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""


class Number:
    MinRadix = 2

    MaxRadix = 36

    @staticmethod
    def urshift(number: int, shift: int):
        return Number.uint(number) >> shift

    @staticmethod
    def uint(number: int) -> int:
        return number if number >= 0 else (number + 0x100000000)
