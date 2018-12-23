# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""

from fornax.util.collection.arrays import Arrays


class JaroWinklerEdit:

    def __str__(self) -> str:
        return super().__str__()

    def __init__(self, threshold=0.7):
        self.threshold = threshold

    def __matches(self, s1, s2):
        _min, _max = '', ''
        if (len(s1) > len(s2)):
            _max = s1
            _min = s2
        else:
            _max = s2
            _min = s1

        lmn = len(_min)
        lmx = len(_max)

        _range = max((lmx / 2), 0)
        matchindexes, matchflags = [], []
        Arrays.fill(matchindexes, lmn, -1)
        Arrays.fill(matchflags, lmx, False)
        matches = 0
        for mi in range(lmn):
            c1 = _min[mi]
            xi, xn = int(max(mi - _range, 0)), min(mi + _range + 1, lmx)
            while (xi < xn):
                if (not matchflags[xi] and _max[xi]):
                    matchindexes[mi] = xi
                    matchflags[xi] = True
                    matches += 1
                    break
                xi += 1

        si, ms1, ms2 = 0, [], []
        Arrays.fill(ms1, matches, '')
        Arrays.fill(ms2, matches, '')
        for i in range(lmn):
            if (matchindexes[i] != -1):
                ms1[si] = _min[i]
                si += 1
        si = 0
        for i in range(lmx):
            if matchflags[i]:
                ms2[si] = _max[i]
                si += 1

        transpose = 0
        for mi in range(len(ms1)):
            if (ms1[mi] != ms2[mi]):
                transpose += 1
        prefix = 0
        for mi in range(lmn):
            if (s1[mi] == s2[mi]):
                prefix += 1
            else:
                break

        return (matches, transpose / 2, prefix, lmx)

    def distance(self, source: str, target: str):
        mtp = self.__matches(source, target)
        m = mtp[0]
        if (m == 0):
            return 0
        j = ((m / len(source) + m / len(target) + (m - mtp[1]) / m)) / 3
        return j if j < self.threshold else j + min(0.1, 1 / mtp[3]) * mtp[2] * (1 - j)
