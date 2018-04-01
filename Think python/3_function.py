#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "xtsheng"

import math
#定义函数
def lyrices():
    print("I'm Andy, and I'm OK.")
    print("I sleep all night and I work all day.")
lyrices()

#函数中套函数
def repeat_lyrices():
    lyrices()
    lyrices()
repeat_lyrices()

#实参
a = math.pow(2,4)
print(a)

#形参
def print_twice(bruce):
    print(bruce)
    print(bruce)
print_twice("Andy") #Andy不加引号就是变量，需要提前定义
print_twice(round(math.pi, 6))

def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
line1 = "Andy"
line2 = "Xu"
cat_twice(line1, line2)

#exercise1
def print_str(s):
    lens = len(s)
    print(" "*(70-lens)+s)
print_str("OK!!!")

#exercise2
def print_plus():
    print("+ "+"- "*4+"+ "+"- "*4+"+")
def print_shu():
    print("|"+" "*9+"|"+" "*9+"|")
def print_4shu():
    print_shu()
    print_shu()
    print_shu()
    print_shu()
def grid():
    print_plus()
    print_4shu()
    print_plus()
    print_4shu()
    print_plus()
grid()