#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(max_integer([2, 1, 5, 3]), 5)
        
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_multipe_max(self):
        self.assertEqual(max_integer([4, 4, 3, 1, 1]), 4)

    def test_floats(self):
        self.assertEqual(max_integer([4.1, 4.2, 3.99, 1.1, 1.5]), 4.2)

    def test_mixed(self):
        self.assertEqual(max_integer([4.1, 4, 3, 1.1, 1.5]), 4.1)

    def test_string(self):
        self.assertEqual(max_integer(['mo', 'rafa', 'none', 'master']), 'rafa')

        
