# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:minus 
@file: test_pharmacy.py
@time: 2018/04/05 
"""
import unittest
import sys

from manage_web import init_driver

sys.path.append('../')


class TestDocApp(unittest.TestCase):
    """
    对 Patient 类进行单元测试
    """

    def setUp(self):
        """
        测试开始: 初始化
        :return:
        """
        self.test_pat = init_driver.TestPat()

    def test_doc_test(self):
        """
        test True for function load_from_file()
        """
        self.test_pat.test_func()

    def tearDown(self):
        """
        测试完毕
        :return:
        """
        self.test_pat = None


if __name__ == '__main__':
    unittest.main()
