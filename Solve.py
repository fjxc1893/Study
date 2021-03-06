#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"
import math

class Solver(object):
    def demo(self, a, b, c):
        """

        :param a:
        :param b:
        :param c:
        :type a: float
        :type b: float
        :type c: float
        :return:
        """
        d = b ** 2 - 4 * a * c
        if d >= 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            print(root1,root2)
            return root1, root2
        else:
            raise Exception

        pass
Solver().demo(2,3,1)