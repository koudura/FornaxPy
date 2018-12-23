# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""
from fornax.util.numerics.number import Number as Num


class Char(object):
    __null = '\0'
    __zero = '0'
    __A = 'a'

    '''
     radix available for conversion to and from strings.
    '''
    maxRadix = 36

    '''
    The minimum radix available for conversion to and from strings.
    '''
    minRadix = 2

    '''
    The constant value of this field is the smallest value of type :'\u005Cu0000'
    '''
    minValue = '\u0000'

    maxValue = '\uFFFF'

    ERROR = 0xFFFFFFFF

    maxCodePoint = 0x10FFFF

    minCodePoint = 0x000000

    minLowSurrogate = '\uDC00'

    maxLowSurrogate = '\uDFFF'

    minHighSurrogate = '\uD800'

    maxHighSurrogate = '\uD8FF'

    maxSurrogate = maxLowSurrogate

    minSurrogate = minHighSurrogate

    MIN_SUPPLEMENTARY_CODE_POINT = 0X010000

    __digitKeys = "0Aa\u0660\u06f0\u0966\u09e6\u0a66\u0ae6\u0b66\u0be7\u0c66\u0ce6\u0d66\u0e50\u0ed0\u0f20\u1040\u1369\u17e0\u1810\uff10\uff21\uff41"

    __digitValues = list(
        "90Z7zW\u0669\u0660\u06f9\u06f0\u096f\u0966\u09ef\u09e6\u0a6f\u0a66\u0aef\u0ae6\u0b6f\u0b66\u0bef\u0be6\u0c6f\u0c66\u0cef\u0ce6\u0d6f\u0d66\u0e59\u0e50\u0ed9\u0ed0\u0f29\u0f20\u1049\u1040\u1371\u1368\u17e9\u17e0\u1819\u1810\uff19\uff10\uff3a\uff17\uff5a\uff37")

    def __init__(self, value: int or str):
        self.__value = chr(value) if type(value) == int else chr(ord(value))

    def value(self) -> str:
        return self.__value

    def valueOf(self, c: int) -> 'Char':
        '''

        :param c:
        :return:
        '''
        return __CharCache__.cache[c] if c <= 127 else Char(c)

    @staticmethod
    def toString(c: int) -> str:
        '''

        :param c:
        :return:
        '''
        return str(Char(c))

    @staticmethod
    def isHighSurrogate(char: int):
        '''

        :param char:
        :return:
        '''
        return ord(Char.minHighSurrogate) <= char <= ord(Char.maxHighSurrogate)

    @staticmethod
    def isLowSurrogate(char: int):
        '''

        :param char:
        :return:
        '''
        return ord(Char.minLowSurrogate) <= char <= ord(Char.maxLowSurrogate)

    @staticmethod
    def isValidCodePoint(codepoint: int) -> bool:
        '''

        :param codepoint:
        :return:
        '''
        plane = Num.urshift(codepoint, 16)
        return plane < (Num.urshift(Char.maxCodePoint + 1, 16))

    @staticmethod
    def isBmpCodePoint(codepoint: int) -> bool:
        '''

        :param codepoint:
        :return:
        '''
        return Num.urshift(codepoint, 16) == 0

    @staticmethod
    def isSupplementaryCodePoint(codepoint: int) -> bool:
        '''

        :param codepoint:
        :return:
        '''
        return (codepoint >= Char.MIN_SUPPLEMENTARY_CODE_POINT and codepoint < (Char.maxCodePoint + 1))

    @staticmethod
    def charCount(codepoint: int) -> int:
        '''

        :param codepoint:
        :return:
        '''
        return 2 if codepoint >= Char.MIN_SUPPLEMENTARY_CODE_POINT else 1

    @staticmethod
    def toCodePoint(high: int, low: int) -> int:
        '''

        :param high:
        :param low:
        :return:
        '''
        _d = (high << 10) + low
        _s = (Char.MIN_SUPPLEMENTARY_CODE_POINT - (ord(Char.minHighSurrogate) << 10) - ord(
            Char.maxLowSurrogate))
        return _d + _s

    @staticmethod
    def codePointAt(charlist: list, index: int, limit: int = None) -> int:
        '''

        :param charlist:
        :param index:
        :param limit:
        :return:
        '''
        if (limit is None): limit = len(charlist)
        if ((index >= limit) or (limit < 0) or (limit > len(charlist))):
            raise IndexError('limit exceeded bounds, index - limit mismatch')
        return Char.__codePointAtImpl(charlist, index, limit)

    @staticmethod
    def __codePointAtImpl(char, index, limit) -> int:
        c1 = char[index]
        index += 1
        if (Char.isHighSurrogate(c1) and index < limit):
            c2 = char[index]
            if (Char.isLowSurrogate(c2)): return Char.toCodePoint(c1, c2)
        return c1

    @staticmethod
    def codePointBefore(charlist: list, index: int, start: int = None) -> int:
        '''

        :param charlist:
        :param index:
        :param start:
        :return:
        '''
        if (start is None): start = 0
        if ((index <= start) or (start < 0) or (start >= len(charlist))):
            raise IndexError('index-start error out of bounds, index - start mismatch')
        return Char.__codePointBeforeImpl(charlist)

    @staticmethod
    def __codePointBeforeImpl(charlist: list, index: int, start: int) -> int:
        index -= 1
        c2 = charlist[index]
        if (Char.isLowSurrogate(c2) and (index > start)):
            index -= 1
            c1 = charlist[index]
            if (Char.isHighSurrogate(c1)):
                return Char.toCodePoint(c1, c2)
        return c2

    def __str__(self) -> str:
        '''

        :return:
        '''
        return str(self.__value)


class __CharCache__:
    '''

    '''
    cache = [Char(c) for c in range(128)]
