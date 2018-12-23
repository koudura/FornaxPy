# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""

import timeit

from fornax.util.text.similarity.jarowinkler import JaroWinklerEdit


if __name__ == '__main__':
    start = timeit.default_timer()
    jedit = JaroWinklerEdit()
    print(jedit.distance('capital', 'capitol'))
    print(jedit.distance('life', 'life'))
    end = timeit.default_timer()
    print((end - start) * 100)
