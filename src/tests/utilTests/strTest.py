# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""

from fornax.util.text.stringtokenizer import StringTokenizer


def testMethod(text):
    tokenizer = StringTokenizer(text)
    caught = []
    while tokenizer.HasMoreTokens():
        token = tokenizer.CurrentToken()
        caught.append(token)
    return caught


if __name__ == '__main__':
    t = """ http://news.google.com The Project Gutenberg EBook of The Time Machine -End of whiteSpace tokenization
            i am the one you want to know how to , i am the 45.6 H.G. wells of rackaracka@youtube.emu, oh lotd vs GOT fags 6, $reef in tug
            $89 users\koudura."""

    print(testMethod(t))
