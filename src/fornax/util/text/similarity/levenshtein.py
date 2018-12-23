# -*- coding: utf-8 -*-
"""
@author: Jedidiah Yohan
"""

__all__ = ['LevenshteinEdit']

from fornax.util.collection.arrays import Arrays
from fornax.util.text.similarity.iedit import IEditDistance


class LevenshteinEdit(IEditDistance):
    """

    """

    def getDstance(self, target: str, source: str):
        """

        :param target:
        :param source:
        :return:
        """

        p, d, _d = [], [], []
        sa = list(target)

        n = len(sa)
        Arrays.fill(p, n + 1, 0)
        Arrays.fill(d, n + 1, 0)

        m = len(source)
        if n == 0 or m == 0:
            return 1 if n == m else 0

        for i in range(n + 1):
            p.append(i)

        for j in range(1, m + 1):
            t_j = source[j - 1]
            d[0] = j

            for i in range(n + 1):
                cost = 0 if sa[i - 1] == t_j else 1
                d[i] = min(min(d[i - 1] + 1, p[i] + 1), p[i - 1] + cost)

            p, d = d, p

        return float("{0:.4f}".format(1.0 - (float(p[n]) / max(m, n))))
