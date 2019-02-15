# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:minus 
@file: TestPat.py
@time: 2018/04/05
"""
import logging
import os
import termcolor
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils import log, config_args
from common import base_methods
from pageobject.manage.login import PageLogin
from common.mock import SetRandom
from pageobject.manage import login

# '''
# 全局给定 日志参数
# '''
# log.init_log("../logs/manage_web")
# red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestInit(object):
    def __init__(self):
        """
        类初始化函数
        """
        self.generate_config = self.generate_user_args(self)
        plantform_dict = self.init_plantform_args()
        user_dict = self.init_user_args()
        user_dict01 = self.init_user_args01()
        self.driver = self.init_driver(plantform_dict)
        self.common_obj = base_methods.BaseMethod(self.driver)
        self.login = self.init_login(self, user_dict)


    @staticmethod
    def generate_user_args(self):
        """
                初始化: 获取 用户 参数
                :return: 参数字典 plantform_config
                """
        user_sec_ops = {
            'user':
                {
                    'username':SetRandom.createUser(self),
                    'phone':SetRandom.createPhone(self),
                    'email':SetRandom.createEmail(self),
                    'url':SetRandom.createUrl(self)
                }
        }
        user_config = config_args.ConfigArgs('../config/users001_conf.ini', user_sec_ops)
        user_config.generate_config()

    @staticmethod
    def init_plantform_args():
        """
        初始化: 获取 测试平台 参数
        :return: 参数字典 plantform_config
        """
        plantom_sec_ops = {
            'testplatform1':
                [
                    'browsername',
                    'URL'
                ]
        }
        plantform_config = config_args.ConfigArgs('../config/plantforms_conf.ini', plantom_sec_ops)
        plantform_config.initialize()
        return plantform_config.config_dict

    @staticmethod
    def init_user_args():
        """
        初始化: 获取 用户 参数
        :return: 参数字典 plantform_config
        """
        user_sec_ops = {
            'user2':
                [
                    'user',
                    'pwd',
                ]
        }
        user_config = config_args.ConfigArgs('../config/users_conf.ini', user_sec_ops)
        user_config.initialize()
        return user_config.config_dict

    @staticmethod
    def init_user_args01():
        """
        初始化: 获取 用户 参数
        :return: 参数字典 plantform_config
        """
        user_sec_ops = {
            'user':
                [
                    'username',
                    'phone',
                    'email',
                    'url',
                ]
        }
        user_config = config_args.ConfigArgs('../config/users001_conf.ini', user_sec_ops)
        user_config.initialize()
        return user_config.config_dict

    @staticmethod
    def init_driver(plantform_dict):
        """
        初始化 webdriver
        :return: driver
        """
        if plantform_dict.get('browsername') == 'Chrome':
            dir = os.path.dirname(os.path.abspath('.'))
            chrome_driver_path = dir + '/tools/chromedriver.exe'
            driver = webdriver.Chrome(chrome_driver_path)
            logging.info('打开谷歌浏览器')
            driver.get(TestInit.init_plantform_args().get('URL'))
            driver.maximize_window()
            return driver
        elif TestInit.init_plantform_args().get('browsername') == 'Firefox':
            driver = webdriver.Firefox()
            logging.info('打开火狐浏览器')
            driver.maximize_window()
            driver.get(TestInit.init_plantform_args().get('URL'))
            logging.info('打开管理端')
            return driver

    def init_login(self,user_dict):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
        self.common_obj.type(PageLogin.user, user_dict.get('user'))
        self.common_obj.type(PageLogin.pwd, user_dict.get('pwd'))
        self.common_obj.click(PageLogin.login)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[1]/a")))
        #要删掉
        self.common_obj.driver.refresh()
        self.common_obj.sleep(3)


