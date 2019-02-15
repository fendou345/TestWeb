# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuxuexue
@file: test_manage.py
@time: 2018/04/05
"""
import unittest
import sys
import termcolor
from utils import log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from manage_web.init_driver import TestInit
from common.base_methods import BaseMethod
from pageobject.manage.login import PageLogin


# sys.path.append('../')
# log.init_log("../logs/manage_web")
# red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestLogin(unittest.TestCase):
    """
    对 Manage 类进行单元测试
    """

    def setUp(self):
        """
        测试开始: 初始化
        :return:
        """
        self.driver = TestInit.init_driver(TestInit.init_plantform_args())

    def test_a_login(self):
        """
        登录成功
        :return:
        """
        base = BaseMethod(self.driver)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
        base.type(PageLogin.user, TestInit.init_user_args().get('user'))
        base.type(PageLogin.pwd, TestInit.init_user_args().get('pwd'))
        base.click(PageLogin.login)
        try:
            self.assertIn('运营后台管理系统', base.getText(PageLogin.title))
        except Exception as e:
            base.getImage()
            raise e

    def test_b_login01(self):
        """
        忘记密码
        :return:
        """
        try:
            base = BaseMethod(self.driver)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "text-primary")))
            base.click(PageLogin.forpwd)
            base.type(PageLogin.phonenum, '13679103525')
            base.click(PageLogin.verification)
            base.sleep(3)
            base.type(PageLogin.veri_num, '8888')
            base.sleep(3)
            base.click(PageLogin.next)

            assert '验证码错误' in base.getText(PageLogin.message)
        except Exception as e:
            base.getImage()
            raise e

    def test_c_login02(self):
        """
        登陆失败_密码错误
        :return:
        """
        try:
            base = BaseMethod(self.driver)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
            base.type(PageLogin.user, TestInit.init_user_args().get('user'))
            base.type(PageLogin.pwd, '111111')
            base.click(PageLogin.login)

            assert '密码不正确' in base.getText(PageLogin.message)
        except Exception as e:
            base.getImage()
            raise e

    def test_d_quit(self):
        """
        退出登录
        :return:
        """
        try:
            base = BaseMethod(self.driver)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#username")))
            base.type(PageLogin.user, TestInit.init_user_args().get('user'))
            base.type(PageLogin.pwd, TestInit.init_user_args().get('pwd'))
            base.click(PageLogin.login)
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/app-root/ng-component/ng-sidebar-container/div/div/nav/div/form[6]/ul/li/a")))
            base.click(PageLogin.user_button)
            base.click(PageLogin.user_quit)
            # alert = self.driver.switch_to.alert()
            # alert.accept()
            base.click(PageLogin.confirm)

            assert '登录' in base.getText(PageLogin.login_title)
        except Exception as e:
            base.getImage()
            raise e

    def tearDown(self):
        """
        测试完毕
        :return:
        """
        self.driver.quit()
