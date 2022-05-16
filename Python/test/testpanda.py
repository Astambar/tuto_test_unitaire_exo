from __future__ import unicode_literals


#coding:utf-8
import unittest
import sys
sys.path.append("..")
from src.panda import Panda

class TestPanda(unittest.TestCase):
    def test_panda_is_instance_of_panda(self):
        p = Panda("Kilo", 15)
        self.assertIsInstance(p, Panda)

    def test_panda_age_is_positive(self):
        p = Panda("Kilo", 15)
        self.assertGreater(p.age, 0)
if __name__=='__main__':
    unittest.main()
