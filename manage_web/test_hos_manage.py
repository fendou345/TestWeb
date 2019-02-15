# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuxuexue
@file: test_hos_manage.py
@time: 2018/04/05
"""
import unittest
import sys
import os
from selenium.webdriver.common.action_chains import ActionChains
from utils import log
from manage_web.init_driver import TestInit
from pageobject.manage.hos_manage import PageHospital
from pageobject.manage.login import PageLogin
from common.current_week import CurrentWeek
import termcolor

# sys.path.append('../')
# log.init_log("../logs/manage_web")
# red_on_cyan = lambda x: termcolor.colored(x, 'red', 'on_cyan')


class TestHospital(unittest.TestCase, TestInit):
    """
    对 医院管理 进行单元测试
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

    def test_a_addhos(self):
        """
        新增医院成功
        :return:
        """
        try:
            self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.hos_info)
            self.common_obj.click(PageHospital.hos_add)
            self.common_obj.sleep(1)
            self.common_obj.type(PageHospital.hos_name, TestInit.init_user_args01().get('username'))
            self.common_obj.type(PageHospital.hos_phone, TestInit.init_user_args01().get('phone'))
            self.common_obj.click(PageHospital.hos_add_province)
            self.common_obj.click(PageHospital.hos_add_province_shanxi)
            self.common_obj.click(PageHospital.hos_add_city)
            self.common_obj.click(PageHospital.hos_add_city_yanan)
            self.common_obj.type(PageHospital.hos_longitude, '111')
            self.common_obj.type(PageHospital.hos_latitude, '111')
            self.common_obj.type(PageHospital.hos_address, TestInit.init_user_args01().get('username'))
            self.common_obj.type(PageHospital.hos_email, TestInit.init_user_args01().get('email'))
            self.common_obj.click(PageHospital.hos_add_level)
            self.common_obj.click(PageHospital.hos_add_level01)
            self.common_obj.click(PageHospital.hos_add_status)
            self.common_obj.click(PageHospital.hos_add_status01)
            self.common_obj.type(PageHospital.hos_url, TestInit.init_user_args01().get('url'))
            self.common_obj.type(PageHospital.hos_postcode, '111')
            self.common_obj.type(PageHospital.hos_portaddress, '111')
            self.common_obj.click(PageHospital.hos_air)
            self.common_obj.click(PageHospital.hos_air)
            path = os.path.dirname(os.path.abspath('.')) + '/image/111.jpg'
            self.common_obj.type(PageHospital.hos_logo, path)
            self.common_obj.type(PageHospital.hos_introduction, '医院简介')
            self.common_obj.click(PageHospital.hos_confirm)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.hos_reset)
            self.common_obj.scrollDown(PageHospital.hos_js)
            if 'true' == self.common_obj.getAttribute(PageHospital.hos_last_page, 'disabled'):
                self.assertIn(TestInit.init_user_args01().get('username'), self.common_obj.getText(PageHospital.hos_result))
            else:
                self.common_obj.click(PageHospital.hos_last_page)
                self.assertIn(TestInit.init_user_args01().get('username'), self.common_obj.getText(PageHospital.hos_result))
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_b_modifyhos(self):
        """
        修改医院成功
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.hos_info)
            self.common_obj.click(PageHospital.hos_reset)
            if 'true' == self.common_obj.getAttribute(PageHospital.hos_last_page, 'disabled'):
                self.common_obj.scrollDown(PageHospital.hos_js)
                self.common_obj.click(PageHospital.hos_id, -1)
                self.common_obj.click(PageHospital.hos_modify)
                self.common_obj.sleep(1)
                self.common_obj.type(PageHospital.hos_name, TestInit.init_user_args01().get('username'))
                self.common_obj.click(PageHospital.hos_confirm)
                self.common_obj.sleep(1)
            else:
                self.common_obj.click(PageHospital.hos_last_page)
                self.common_obj.scrollDown(PageHospital.hos_js)
                self.common_obj.click(PageHospital.hos_id, -1)
                self.common_obj.click(PageHospital.hos_modify)
                self.common_obj.sleep(1)
                self.common_obj.type(PageHospital.hos_name, TestInit.init_user_args01().get('username'))
                self.common_obj.click(PageHospital.hos_confirm)
                self.common_obj.sleep(1)
                self.common_obj.click(PageHospital.hos_last_page)
            self.common_obj.scrollDown(PageHospital.hos_js)
            self.assertIn(TestInit.init_user_args01().get('username'), self.common_obj.getText(PageHospital.hos_id, -1))
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_c_queryhos(self):
        """
        查询医院，查询条件单选（医院名称）
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.hos_info)
            self.common_obj.click(PageHospital.hos_reset)
            self.common_obj.type(PageHospital.hos_query_name, TestInit.init_user_args01().get('username'))
            self.common_obj.click(PageHospital.hos_query)
            self.assertEqual(TestInit.init_user_args01().get('username'), self.common_obj.getText(PageHospital.hos_query_name_result))
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_d_queryhos01(self):
        """
        查询医院，查询条件单选（状态）
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.hos_info)
            self.common_obj.click(PageHospital.hos_reset)
            self.common_obj.click(PageHospital.hos_status)
            self.common_obj.click(PageHospital.hos_status01)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.hos_show_num)
            self.common_obj.click(PageHospital.hos_show_num01)
            while None == self.common_obj.getAttribute(PageHospital.hos_next_page, 'disabled'):
                self.assertEqual("已上线", self.common_obj.getText(PageHospital.hos_query_status_result, 111))
                self.common_obj.click(PageHospital.hos_next_page)

            else:
                self.assertEqual("已上线", self.common_obj.getText(PageHospital.hos_query_status_result, 111))
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_e_queryhos02(self):
        """
        查询医院，查询条件多选（省、市、状态）
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.hos_info)
            self.common_obj.click(PageHospital.hos_reset)
            self.common_obj.click(PageHospital.hos_province)
            self.common_obj.click(PageHospital.hos_province_shanxi)
            self.common_obj.click(PageHospital.hos_city)
            self.common_obj.click(PageHospital.hos_city_yanan)
            self.common_obj.click(PageHospital.hos_status)
            self.common_obj.click(PageHospital.hos_status01)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.hos_show_num)
            self.common_obj.click(PageHospital.hos_show_num01)
            while None == self.common_obj.getAttribute(PageHospital.hos_next_page, 'disabled'):
                el = self.common_obj.find_element(PageHospital.hos_query_status_result, 111)
                for i in range(len(el)):
                    el[i].click()
                    self.common_obj.click(PageHospital.hos_modify)
                    self.assertEqual("陕西省", self.common_obj.getText(PageHospital.hos_province_text))
                    self.assertEqual("延安市", self.common_obj.getText(PageHospital.hos_city_text))
                    self.assertEqual("已上线", self.common_obj.getText(PageHospital.hos_status_text))
                    self.common_obj.click(PageHospital.hos_cancel)
                self.common_obj.click(PageHospital.hos_next_page)
            else:
                el = self.common_obj.find_element(PageHospital.hos_query_status_result, 111)
                for i in range(len(el)):
                    el[i].click()
                    self.common_obj.click(PageHospital.hos_modify)
                    self.assertEqual("陕西省", self.common_obj.getText(PageHospital.hos_province_text))
                    self.assertEqual("延安市", self.common_obj.getText(PageHospital.hos_city_text))
                    self.assertEqual("已上线", self.common_obj.getText(PageHospital.hos_status_text))
                    self.common_obj.click(PageHospital.hos_cancel)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_f_deletedept(self):
        """
        删除科室
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.dept_info)
            self.common_obj.click(PageHospital.dept_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.click(PageHospital.dept_test)
            self.common_obj.click(PageHospital.dept_deptname)
            self.common_obj.click(PageHospital.dept_delete)
            self.common_obj.click(PageHospital.dept_add_confirm)
            assert "麻醉科" not in self.common_obj.getText(PageHospital.dept_result)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)


    def test_g_adddept(self):
        """
        新增科室（五官科-麻醉科）
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.dept_info)
            self.common_obj.click(PageHospital.dept_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.click(PageHospital.dept_test)
            self.common_obj.click(PageHospital.dept_add)
            self.common_obj.click(PageHospital.dept_test01)
            self.common_obj.click(PageHospital.dept_add_confirm)
            assert "麻醉科" in self.common_obj.getText(PageHospital.dept_deptname)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_h_modifydept(self):
        """
        修改科室
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.dept_info)
            self.common_obj.click(PageHospital.dept_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.click(PageHospital.dept_test)
            self.common_obj.click(PageHospital.dept_test01)
            self.common_obj.click(PageHospital.dept_modify)
            self.common_obj.type(PageHospital.dept_introduction, TestInit.init_user_args01().get('username'))
            self.common_obj.click(PageHospital.dept_add_confirm)
            assert "执行成功" in self.common_obj.getText(PageLogin.message)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_i_guidedept(self):
        """
        导诊科室维护
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.dept_info)
            self.common_obj.click(PageHospital.dept_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.click(PageHospital.dept_test)
            self.common_obj.click(PageHospital.dept_test01)
            self.common_obj.click(PageHospital.dept_guide)
            self.common_obj.click(PageHospital.dept_guide_expand)
            self.common_obj.click(PageHospital.dept_guide_dept)
            self.common_obj.click(PageHospital.dept_add_confirm)
            assert "血管外科" in self.common_obj.getText(PageHospital.dept_guidename)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_j_detaildoc(self):
        """
        医生详情-上传图片成功
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.doc_info)
            self.common_obj.click(PageHospital.doc_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.doc_expand)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.doc_expand_test)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.doc_dept)
            self.common_obj.click(PageHospital.doc_info_detail)
            self.common_obj.click(PageHospital.doc_detail)
            path = os.path.dirname(os.path.abspath('.')) + '/image/111.jpg'
            self.common_obj.type(PageHospital.doc_image, path)
            self.common_obj.click(PageHospital.doc_close)
            assert "上传成功" in self.common_obj.getText(PageLogin.message)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_k_querydoc(self):
        """
        医生查询
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.doc_info)
            self.common_obj.click(PageHospital.doc_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.doc_expand)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.doc_expand_test)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.doc_dept)
            self.common_obj.type(PageHospital.doc_query, '梁栋')
            assert "梁栋" in self.common_obj.getText(PageHospital.doc_name)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_l_addschedu(self):
        """
        新增排班(给当天排)
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.schedu)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.click(PageHospital.schedu_add)
            self.common_obj.type(PageHospital.avg_time, '10')
            self.common_obj.click(PageHospital.avg_time_update)
            self.common_obj.click(PageHospital.registered_type)
            self.common_obj.click(PageHospital.registered_type01)
            self.common_obj.click(PageHospital.time)
            self.common_obj.click(PageHospital.time_am)
            source = self.common_obj.find_element(PageHospital.schedu_doc)
            target = self.common_obj.find_element(PageHospital.schedu_time_today)
            ActionChains(self.driver).drag_and_drop(source, target).perform()
            assert "不能排班与当天以及之前" in self.common_obj.getText(PageLogin.message)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_m_addschedu01(self):
        """
        新增排班(给明天排，上午一个医生排两次)
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.schedu)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.click(PageHospital.schedu_add)
            self.common_obj.type(PageHospital.avg_time, '10')
            self.common_obj.click(PageHospital.avg_time_update)
            self.common_obj.click(PageHospital.registered_type)
            self.common_obj.click(PageHospital.registered_type01)
            self.common_obj.click(PageHospital.time)
            self.common_obj.click(PageHospital.time_am)

            source = self.common_obj.find_element(PageHospital.schedu_doc)
            if '星期六' == CurrentWeek.currentWeek(self):
                self.common_obj.click(PageHospital.next_week)
                target = self.common_obj.find_element(PageHospital.schedu_time_tomorrow01)
            else:
                target = self.common_obj.find_element(PageHospital.schedu_time_tomorrow02)
            ActionChains(self.driver).drag_and_drop(source, target).perform()

            self.common_obj.sleep(2)

            source = self.common_obj.find_element(PageHospital.schedu_doc01)
            if '星期六' == CurrentWeek.currentWeek(self):
                self.common_obj.click(PageHospital.next_week)
                target = self.common_obj.find_element(PageHospital.schedu_time_tomorrow01)
            else:
                target = self.common_obj.find_element(PageHospital.schedu_time_tomorrow02)
            ActionChains(self.driver).drag_and_drop(source, target).perform()

            assert "同一人，同一日，上午或下午，不能再排" in self.common_obj.getText(PageLogin.message)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_n_addschedu02(self):
        """
        新增排班(给明天排，上午一个医生排一次)
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.schedu)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.click(PageHospital.schedu_add)
            self.common_obj.type(PageHospital.avg_time, '10')
            self.common_obj.click(PageHospital.avg_time_update)
            self.common_obj.click(PageHospital.registered_type)
            self.common_obj.click(PageHospital.registered_type01)
            self.common_obj.click(PageHospital.time)
            self.common_obj.click(PageHospital.time_am)
            source = self.common_obj.find_element(PageHospital.schedu_doc)
            if '星期六' == CurrentWeek.currentWeek(self):
                self.common_obj.click(PageHospital.next_week)
                target = self.common_obj.find_element(PageHospital.schedu_time_tomorrow01)
            else:
                target = self.common_obj.find_element(PageHospital.schedu_time_tomorrow02)
            ActionChains(self.driver).drag_and_drop(source, target).perform()
            self.common_obj.click(PageHospital.schedu_save)

            if '星期六' == CurrentWeek.currentWeek(self):
                self.common_obj.click(PageHospital.next_week)
            assert "石丹丹" in self.common_obj.getText(PageHospital.save_result)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_o_deleteschedu(self):
        """
        删除排班(删除新增排班增加的排班)
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.schedu)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.sleep(1)
            if '星期六' == CurrentWeek.currentWeek(self):
                self.common_obj.click(PageHospital.next_week)
            self.common_obj.click(PageHospital.schedu_delete)
            self.common_obj.click(PageHospital.schedu_delete_confirm)

            assert "石丹丹" not in self.common_obj.getText(PageHospital.save_result)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_p_add_deptprice(self):
        """
        新增科室挂号费(体检科)
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.deptprice)
            self.common_obj.click(PageHospital.price_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.price_dept)
            self.common_obj.click(PageHospital.price_add)
            self.common_obj.click(PageHospital.treat_type)
            self.common_obj.click(PageHospital.treat_type01)
            self.common_obj.type(PageHospital.price, '1')
            self.common_obj.click(PageHospital.price_confirm)

            assert "普通号" in self.common_obj.getText(PageHospital.price_result)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_q_modify_deptprice(self):
        """
        修改科室挂号费(体检科)
       :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.deptprice)
            self.common_obj.click(PageHospital.price_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.price_dept)
            self.common_obj.click(PageHospital.price_info)
            self.common_obj.click(PageHospital.price_modify)
            self.common_obj.type(PageHospital.price, TestInit.init_user_args01().get('phone'))
            self.common_obj.click(PageHospital.price_confirm)
            assert TestInit.init_user_args01().get('phone') in self.common_obj.getText(PageHospital.price_info_price)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)

    def test_r_delete_deptprice(self):
        """
        删除科室挂号费(体检科)
        :return:
        """
        try:
            #self.common_obj.click(PageHospital.hos_manage)
            self.common_obj.click(PageHospital.deptprice)
            self.common_obj.click(PageHospital.price_reset)
            self.common_obj.click(PageHospital.dept_province)
            self.common_obj.click(PageHospital.dept_province_shanxi)
            self.common_obj.click(PageHospital.dept_city)
            self.common_obj.click(PageHospital.dept_city_xian)
            self.common_obj.click(PageHospital.dept_level)
            self.common_obj.click(PageHospital.dept_level01)
            self.common_obj.click(PageHospital.dept_hos)
            self.common_obj.click(PageHospital.dept_hos01)
            self.common_obj.sleep(1)
            self.common_obj.click(PageHospital.price_dept)
            self.common_obj.click(PageHospital.price_info01)
            self.common_obj.click(PageHospital.price_delete)
            self.common_obj.click(PageHospital.price_delete_confirm)
            assert "普通号" not in self.common_obj.getText(PageHospital.price_result)
        except Exception as e:
            self.common_obj.getImage()
            print('Test Fail', format(e))
        self.common_obj.sleep(2)






