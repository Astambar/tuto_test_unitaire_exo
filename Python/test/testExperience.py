#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import unittest
sys.path.append('../')
from fonction import *

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add.add(1,2), 3)
    def test_sub(self):
        self.assertEqual(sub.sub(1,2), -1)
    def test_div(self):
        self.assertEqual(div.div(1,2), 0.5)
    def test_mul(self):
        self.assertEqual(mul.mul(1,2), 2)
    def test_squared(self):
        self.assertEqual(squared.squared(2), 4)
    def test_pow(self):
        self.assertEqual(pow.pow(3,2), 9)
    def test_modulo(self):
        self.assertEqual(modulo.modulo(3,2), 1)
    def test_modulo(self):
        self.assertEqual(modulo.modulo(3,3), 0)
    def test_str_concat(self):
        self.assertEqual(str_concat.str_concat('3','2'), '32')
    def test_add(self):
        self.assertEqual(loop_function.loop_function('add',0,1,1), "erreur")
    def test_squared(self):
        self.assertEqual(loop_function.loop_function('squared',3,5), 25)

if __name__ == '__main__':
    unittest.main()
