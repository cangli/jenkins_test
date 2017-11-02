#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:38:46 2017

@author: gabriel
"""

import unittest
from add_func import add


class TestAddFunc(unittest.TestCase):
    def test_add_func(self):
        self.assertEqual(add(3, 5), 8)


if __name__ == '__main__':
    unittest.main()
