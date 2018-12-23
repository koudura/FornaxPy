# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""
import fornax.util.const as const
from fornax.util.text.character import Char


class StringTokenizer(object):
    """
    The "StringTokenizer" class allows an application to break a string into tokens by performing code
    point comparison. The :see:"StringTokenizer" methods do not distinguish among identifiers,
    numbers, and quoted strings, nor do they recognize and skip comments.
    """

    def __init__(self, text: str, delimiters: str = const.Delimiter.default, returnDelims: bool = False):
        """
        Initializes a new instance of the :see: "StringTokenizer" class.
        Using specified characters in @param:"delim" as delimiters.
        @param:"returnDelim" determines if delimiters are treated as tokens.
        :param text: The string to tokenize.
        :param delimiters: The delimiters as string.
        :param returnDelims: if set to True, delimiters would be return as tokens, else not.
        """
        if text is not None:
            self.__currentPosition = 0
            self.__newPosition = -1
            self.__delimsChanged = False
            self.text = text
            self.__maxPosition = len(text)
            self.__delimiters = delimiters
            self.__returnDelims = returnDelims
            self.__hasSurrogates = False
            self.__setMaxDelimCodePoint()
        else:
            raise Exception('text input cannot be None')

    def __setMaxDelimCodePoint(self):
        '''
        Sets the maximum delimiter code point to the highest character in the delimiter set.
        :return:
        '''
        if self.__delimiters is None:
            self.__maxdelimCodepoint = 0
            return
        c, m, count = 0, 0, 0
        for i in range(0, len(self.__delimiters), Char.charCount(c)):
            c = ord(self.__delimiters[i])
            if ord(Char.minHighSurrogate) <= c <= ord(Char.maxLowSurrogate):
                c = Char.codePointAt(list(self.__delimiters), i)
                self.__hasSurrogates = True
            if m < c:
                m = c
            count += 1
        self.__maxdelimCodepoint = m
        if self.__hasSurrogates:
            self.__delimCodePoints = []
            j = 0
            for i in range(count):
                c = Char.codePointAt(list(self.__delimiters), j)
                self.__delimCodePoints[i] = c
                j += Char.charCount(c)
        print('endmaxxodepoint')

    def __skipDelimiters(self, start: int) -> int:
        '''
        Skips the delimiters
        :param start: the start position
        :return:
        '''
        if self.__delimiters is None: raise Exception('Null Reference Exception -m delimiter cannot be null')

        position = start
        while (not self.__returnDelims) and (position < self.__maxPosition):
            if not self.__hasSurrogates:
                c = ord(self.text[position])
                if (c > self.__maxdelimCodepoint) or (self.text[position] not in self.__delimiters):
                    break
                else:
                    position += 1
            else:
                c = Char.codePointAt(list(self.text), position)
                if (c > self.__maxdelimCodepoint) or not self.__isDelimiter(c): break
                position += Char.charCount(c)
        return position

    def __isDelimiter(self, codepoint: int) -> bool:
        """
        Determines whether the specified code point is delimiter.
        :param codepoint: the code point
        :return: True, if the specified codepoint is delimiter; otherwise False.
        """
        for i in range(len(self.__delimCodePoints)):
            if self.__delimCodePoints[i] == codepoint: return True
        return False

    def __scanTokens(self, start: int) -> int:
        """
        Skips ahead from @param:start and returns the index of the next delimiter
        character encountered, @max-position if no such delimiter is found.
        :param start: the START position.
        :return: position of found character.
        """
        position = start
        while position < self.__maxPosition:
            if not self.__hasSurrogates:
                c = ord(self.text[position])
                if c <= self.__maxdelimCodepoint and (self.text[position] in self.__delimiters): break
                position += 1
            else:
                c = Char.codePointAt(list(self.text), position)
                if (c <= self.__maxdelimCodepoint) and self.__isDelimiter(c): break
                position += Char.charCount(c)

        if self.__returnDelims and (start == position):
            if not self.__hasSurrogates:
                c = ord(self.text[position])
                if c <= self.__maxdelimCodepoint and (c in self.__delimiters):
                    position += 1
            else:
                c = Char.codePointAt(list(self.text), position)
                if c <= self.__maxdelimCodepoint and self.__isDelimiter(c):
                    position += Char.charCount(c)
        return position

    def CurrentToken(self) -> str:
        """
        Returns the current token from this string tokenizer.
        :return: the current token from this string tokenizer
        """
        self.__currentPosition = self.__newPosition if (
                self.__newPosition >= 0 and not self.__delimsChanged) else self.__skipDelimiters(
            self.__currentPosition)
        self.__delimsChanged = False
        self.__newPosition = -1

        if self.__currentPosition >= self.__maxPosition: raise IndexError('Index out of bounds exception.')
        start = self.__currentPosition
        self.__currentPosition = self.__scanTokens(self.__currentPosition)
        return self.text[start:self.__currentPosition + 1]

    def NextToken(self, delimiter: str) -> str:
        """
        Returns the next tokens after changing the delimiters.
        :param delimiter: The new delimiters.
        :return: The next token in enumeration.
        """
        self.__delimiters = delimiter
        self.__delimsChanged = True

        self.__setMaxDelimCodePoint()
        return self.CurrentToken()

    def HasMoreTokens(self) -> bool:
        """
        Tests if there are more tokens available from this tokenizer's string.
        If this method returns <True>, then a subsequent call to :see="NextToken"
        will successfully return a token.
        :return: :True if and only if there is at least one token in the string after the current position
         ;otherwise, :False
        """
        self.__newPosition = self.__skipDelimiters(self.__currentPosition)
        return self.__newPosition < self.__maxPosition

    def HasMoreElments(self) -> bool:
        """
        Returns the same value as the "HasMoreTokens()" method.
        :return: True, if and only if there is at least one token in the string after the current position
         ;otherwise,False
        """
        return self.HasMoreTokens()

    def CurrentElement(self) -> object:
        """
         Returns the value as the "NextToken()" method, except that its declared value is
        :return:
        """
        return self.CurrentToken()

    def CountTokens(self) -> int:
        """
        Calculates the number of times that this tokenizer's "NextToken()" method can be called before
        it generates an exception. The current position is not advanced.
        :return: The number of tokens remaining in the string using the current delimiter set.
        """
        count = 0
        currentpos = self.__currentPosition
        while currentpos < self.__maxPosition:
            currentpos = self.__skipDelimiters(currentpos)
            if currentpos >= self.__maxPosition: break
            currentpos = self.__scanTokens(currentpos)
            count += 1
        return count
