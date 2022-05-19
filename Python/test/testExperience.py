#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import unittest
sys.path.append('../')
from fonction.functione import functione as fct
from fonction.loop_function import loop_function

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(fct('add')(1,2), 3)
    def test_sub(self):
        self.assertEqual(fct('sub')(1,2), -1)
    def test_div(self):
        self.assertEqual(fct('div')(1,2), 0.5)
    def test_mul(self):
        self.assertEqual(fct('mul')(1,2), 2)
    def test_squared(self):
        self.assertEqual(fct('squared')(2), 4)
    def test_pow(self):
        self.assertEqual(fct('pow')(3,2), 9)
    def test_modulo(self):
        self.assertEqual(fct('modulo')(3,2), 1)
    def test_modulo(self):
        self.assertEqual(fct('modulo')(3,3), 0)
    def test_str_concat(self):
        self.assertEqual(fct('str_concat')('3','2'), '32')
        """_loop_ test
        """
    def test_loop_function_repeat_negative(self):
        self.assertEqual(loop_function('add',-1,1,1), "erreur")
    def test_loop_add(self):
        self.assertEqual(loop_function('add',2,1,1), 3)    
    def test_loop_squared(self):
        self.assertEqual(loop_function('squared',2,5), 625)
    def test_loop_sub(self):
        self.assertEqual(loop_function('sub',1,1,1), 0)
    def test_loop_div(self):
        self.assertEqual(loop_function('div',2,5,5), 0.2)
    

if __name__ == '__main__':
    unittest.main()
