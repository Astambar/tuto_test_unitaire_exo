#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import sys
from fonction import add, sub, mul, div, squared, pow

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

if __name__ == '__main__':
    unittest.main()
