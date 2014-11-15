#!/usr/bin/env python3
import metric
import unittest


class TestMetric(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_noop(self):
        '''Test no-op'''
        pass

    def test_used_memory(self):
        '''Test getting used memory metric'''
        used = metric.used_memory()

