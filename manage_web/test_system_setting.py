# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuxuexue
@file: test_system_setting.py
@time: 2018/04/05
"""
import unittest
import sys
from utils import log
from manage_web.init_driver import TestInit
from pageobject.manage.system_setting import PageSetting
from pageobject.manage.login import PageLogin
import termcolor

# sys.path.append('../')
# log.init_log("../logs/manage_web")
# red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestSetting(unittest.TestCase, TestInit):
    """
    对 系统设置 进行单元测试
    """

    @classmethod
    def setUpClass(cls):
        """
        测试开始: 初始化
        :return:
        """
        TestInit.__init__(cls)

    @classmethod
    def tearDownClass(cls):
        """
        测试完毕
        :return:
        """
        cls.driver.quit()

    def test_a_addperson(self):
        """
        新增人员成功
        :return:
        """
        try:
            self.common_obj.click(PageSetting.sys_setting)

            self.common_obj.click(PageSetting.person_manage)

            self.common_obj.click(PageSetting.product)

            self.common_obj.click(PageSetting.add)

            self.common_obj.type(PageSetting.add_phonenum, TestInit.init_user_args01().get("phone"))

            self.common_obj.type(PageSetting.add_name, TestInit.init_user_args01().get('username'))

            self.common_obj.type(PageSetting.add_card, '340402197303110018')

            self.common_obj.click(PageSetting.add_sex)

            self.common_obj.click(PageSetting.sex_women)

            self.common_obj.type(PageSetting.add_email, TestInit.init_user_args01().get('email'))

            self.common_obj.type(PageSetting.add_user, TestInit.init_user_args01().get('username'))
            self.common_obj.click(PageSetting.start)

            self.common_obj.click(PageSetting.role1)

            self.common_obj.click(PageSetting.hospital)

            self.common_obj.click(PageSetting.add_save)

            self.common_obj.click(PageSetting.product)

            if 'true' == self.common_obj.getAttribute(PageSetting.person_last_page, 'disabled'):
                assert TestInit.init_user_args01().get("phone") in self.common_obj.getText(PageSetting.result)
            else:
                self.common_obj.click(PageSetting.person_last_page)
                assert TestInit.init_user_args01().get("phone") in self.common_obj.getText(PageSetting.result)
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_b_addperson01(self):
        """
        新增人员失败-手机号已存在
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)

            self.common_obj.click(PageSetting.person_manage)

            self.common_obj.click(PageSetting.product)

            self.common_obj.click(PageSetting.add)
            self.common_obj.sleep(2)
            self.common_obj.type(PageSetting.add_phonenum, '13679103525')

            self.common_obj.click(PageSetting.add_name)

            assert "账号已存在" in self.common_obj.getText(PageLogin.message)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_c_addperson02(self):
        """
        新增人员失败-姓名校验
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)

            self.common_obj.click(PageSetting.person_manage)

            self.common_obj.click(PageSetting.product)

            self.common_obj.click(PageSetting.add)

            self.common_obj.type(PageSetting.add_name, 'aaaaaaaa')

            assert '名字长度为1-5个字符' in self.common_obj.getText(PageSetting.name_check)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_d_modifyperson(self):
        """
        修改人员信息成功
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)

            self.common_obj.click(PageSetting.person_manage)

            self.common_obj.click(PageSetting.product)
            if 'true' == self.common_obj.getAttribute(PageSetting.person_last_page, 'disabled'):
                self.common_obj.scrollDown(PageSetting.sys_js)
                self.common_obj.click(PageSetting.person, -1)
                self.common_obj.click(PageSetting.modify)
                self.common_obj.click(PageSetting.role2)
                self.common_obj.click(PageSetting.add_save)
                self.common_obj.click(PageSetting.product)
            else:
                self.common_obj.click(PageSetting.person_last_page)
                self.common_obj.scrollDown(PageSetting.sys_js)
                self.common_obj.click(PageSetting.person, -1)
                self.common_obj.click(PageSetting.modify)
                self.common_obj.click(PageSetting.role2)
                self.common_obj.click(PageSetting.add_save)
                self.common_obj.click(PageSetting.product)
                self.common_obj.click(PageSetting.person_last_page)

            self.common_obj.scrollDown(PageSetting.sys_js)
            assert '商品管理' in self.common_obj.getText(PageSetting.person, -1)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_e_deleteperson(self):
        """
        删除人员信息成功
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)

            self.common_obj.click(PageSetting.person_manage)

            self.common_obj.click(PageSetting.product)
            if 'true' == self.common_obj.getAttribute(PageSetting.person_last_page, 'disabled'):
                self.common_obj.scrollDown(PageSetting.sys_js)
                self.common_obj.click(PageSetting.person, -1)
                self.common_obj.click(PageSetting.delete)
                self.common_obj.click(PageSetting.delete_confirm)
            else:
                self.common_obj.click(PageSetting.person_last_page)
                self.common_obj.scrollDown(PageSetting.sys_js)
                self.common_obj.click(PageSetting.person, -1)
                self.common_obj.click(PageSetting.delete)
                self.common_obj.click(PageSetting.delete_confirm)
                self.common_obj.click(PageSetting.person_last_page)

            self.common_obj.scrollDown(PageSetting.sys_js)
            assert 'pl-2 fa fa-close' in self.common_obj.getAttribute(PageSetting.person, 'class', -1)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_f_addrole(self):
        """
        新增角色成功
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.role_manage)
            self.common_obj.click(PageSetting.role_add)
            self.common_obj.type(PageSetting.role_name, TestInit.init_user_args01().get('username'))
            self.common_obj.type(PageSetting.role_note,'测试备注001')
            self.common_obj.click(PageSetting.add_save)

            assert TestInit.init_user_args01().get('username') in self.common_obj.getText(PageSetting.result)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_g_addrole01(self):
        """
        新增角色失败-角色名已存在
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.role_manage)
            self.common_obj.click(PageSetting.role_add)
            self.common_obj.type(PageSetting.role_name,'医院管理')
            self.common_obj.click(PageSetting.add_save)

            assert "该角色名已存在" in self.common_obj.getText(PageLogin.message)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_h_modifyrole(self):
        """
        修改角色成功
        :return:
        """
        try:
            # self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.role_manage)
            self.common_obj.click(PageSetting.role_delete_info)
            self.common_obj.click(PageSetting.role_modify)
            self.common_obj.type(PageSetting.role_note, TestInit.init_user_args01().get('username'))
            self.common_obj.click(PageSetting.add_save)

            assert TestInit.init_user_args01().get('username') in self.common_obj.getText(PageSetting.result)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_i_deleterole(self):
        """
        删除角色成功
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.role_manage)
            self.common_obj.click(PageSetting.role_delete_info)
            self.common_obj.click(PageSetting.role_delete)
            self.common_obj.click(PageSetting.delete_confirm)

            assert '测试备注001' not in self.common_obj.getText(PageSetting.result)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_j_deleterole01(self):
        """
        删除角色失败
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.role_manage)
            self.common_obj.click(PageSetting.role_delete_info1)
            self.common_obj.click(PageSetting.role_delete)
            self.common_obj.click(PageSetting.delete_confirm)

            assert "该角色下存在用户不能被删除" in self.common_obj.getText(PageLogin.message)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_k_adddept(self):
        """
        新增部门成功
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.dept_manage)
            self.common_obj.click(PageSetting.dept_add)
            self.common_obj.type(PageSetting.dept_name, TestInit.init_user_args01().get('username'))
            self.common_obj.type(PageSetting.dept_note,'测试备注001')
            self.common_obj.click(PageSetting.dept_add_save)

            assert TestInit.init_user_args01().get('username') in self.common_obj.getText(PageSetting.result)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_l_modifydept(self):
        """
        修改部门成功
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.dept_manage)
            self.common_obj.click(PageSetting.dept_delete_info)
            self.common_obj.click(PageSetting.dept_modify)
            self.common_obj.type(PageSetting.dept_name, TestInit.init_user_args01().get('username'))
            self.common_obj.click(PageSetting.dept_add_save)

            assert TestInit.init_user_args01().get('username') in self.common_obj.getText(PageSetting.result)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_m_deletedept(self):
        """
        删除部门成功
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.dept_manage)
            self.common_obj.click(PageSetting.dept_delete_info)
            self.common_obj.click(PageSetting.dept_delete)
            self.common_obj.sleep(1)
            self.common_obj.click(PageSetting.delete_confirm)

            assert '测试备注001' not in self.common_obj.getText(PageSetting.result)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_n_deletedept01(self):
        """
        删除部门失败
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.dept_manage)
            self.common_obj.click(PageSetting.dept_delete_info1)
            self.common_obj.click(PageSetting.dept_delete)
            self.common_obj.sleep(1)
            self.common_obj.click(PageSetting.delete_confirm)

            assert "组织机构信息无法删除" in self.common_obj.getText(PageLogin.message)
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)

    def test_o_modifysys(self):
        """
        修改系统参数成功
        :return:
        """
        try:
            #self.common_obj.click(PageSetting.sys_setting)
            self.common_obj.click(PageSetting.sys_para)
            self.common_obj.click(PageSetting.sys_sms)
            self.common_obj.type(PageSetting.sys_sms_set,TestInit.init_user_args01().get('username'))
            self.common_obj.click(PageSetting.sys_save)
            self.common_obj.click(PageSetting.sys_confirm)

            assert TestInit.init_user_args01().get('username') in self.common_obj.getAttribute(PageSetting.sys_sms_set, 'ng-reflect-model')
            print("Test Sucess")
        except Exception as e:
            self.common_obj.getImage()
            raise e
        self.common_obj.sleep(2)


