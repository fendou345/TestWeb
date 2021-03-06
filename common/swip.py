# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:liuxuexue
@file: swip.py 
@time: 2018/04/05 
"""


class Swip(object):
    def __init__(self, driver):
        self.driver = driver

    def get_size(self):
        """
        获得机器屏幕大小x,y
        :return:
        """
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    def swipe_up(self, t):
        """
        屏幕向上滑动,t表示时间，ms
        :param t:
        :return:
        """
        l= self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t):
        """
        屏幕向下滑动
        :param t:
        :return:
        """
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)

    def swip_left(self, t):
        """
        屏幕向左滑动
        :param t:
        :return:
        """
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)

    def swip_right(self, t):
        """
        屏幕向右滑动
        :param t:
        :return:
        """
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)
