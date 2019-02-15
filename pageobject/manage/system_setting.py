# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuxuexue
@file: test_login.py
@time: 2018/04/08
"""

class PageSetting(object):
    """
    与系统有关元素
    """
    #系统设置按钮
    sys_setting = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[1]/a'
    #人员管理按钮
    person_manage = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[1]/treeview-menu/ul/li[1]/a'
    #朔维公司下的开发部
    product = 'xpath=>//tree-node-content/label/span[text()="开发部"]'
    #人员管理——新增
    add = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-employee/div/grid-action/div/div/div/button[1]'
    # 人员管理——新增-手机号
    add_phonenum = 'css_selector=>#phone'
    # 人员管理——新增-姓名
    add_name = 'css_selector=>#name'
    # 人员管理——新增-身份证号
    add_card = 'css_selector=>#idNo'
    # 人员管理——新增-性别
    add_sex = 'css_selector=>#sex'
    #人员管理——新增-性别-女
    sex_women = 'xpath=>//sui-select/div/sui-select-option[2]'
    #人员管理——新增-邮箱
    add_email = 'css_selector=>#email'
    # 人员管理——新增-账号
    add_user = 'css_selector=>#username'
    #人员管理——新增-启用
    start = 'css_selector=>#enable'
    # 人员管理——新增-角色选择树-医院管理
    role1 = 'xpath=>//tree-node-content/label/span[text()="医院管理"]'
    role2 = 'xpath=>//tree-node-content/label/span[text()="商品管理"]'
    hospital = 'xpath=>//tree-node-content/label/span[text()="西安交通大学第一附属医院"]'
    # 人员管理——新增-保存
    add_save = 'xpath=>//div/button[text()="保存"]'
    #人员管理-末页
    person_last_page = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-employee/div/div/div[2]/app-base-grid/div/div[2]/app-grid-bbar/nav/form/button[4]'
    #期望结果-手机号
    result = 'class_name=>demo-contents'
    #期望结果-姓名校验
    name_check = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-employee-edit/div/div[1]/div[1]/div[2]/div/form/div[3]/div/p'
    #选择最后一个人员信息
    person = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[1]/div/div'
    #人员管理——修改
    modify = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-employee/div/grid-action/div/div/div/button[2]'
    #人员管理——删除
    delete = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-employee/div/grid-action/div/div/div/button[3]'
    #人员管理-删除-确定
    delete_confirm = 'class_name=>primary'
    # 人员管理-人员信息表格框向下滚动
    sys_js = "var q=document.getElementsByClassName('ag-body')[0].scrollTop=10000"

    #角色管理
    role_manage = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[1]/treeview-menu/ul/li[2]/a/span'
    #角色管理-新增
    role_add = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-role/div/grid-action/div/div/div/button[1]'
    #角色管理-超级管理员
    super_manager = '//tree-node-content/label/span[text()="超级管理员"]'
    #角色管理-新增-名称
    role_name = 'css_selector=>#name'
    # 角色管理-新增-备注
    role_note = 'css_selector=>#code'
    #角色管理-新增-权限
    role_permission = 'xpath=>//tree-node-content/label/span[text()="人员管理"]'
    #角色管理-修改
    role_modify = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-role/div/grid-action/div/div/div/button[2]'
    #角色管理-删除
    role_delete = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-role/div/grid-action/div/div/div/button[3]'
    #角色管理-删除/修改-备注为测试备注001的记录
    role_delete_info = 'xpath=>//div[text()="测试备注001"]'
    # 角色管理-删除-角色名称为医院管理的记录
    role_delete_info1 = 'xpath=>//div[text()="测试无法删除"]'

    #部门管理
    dept_manage = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[1]/treeview-menu/ul/li[3]/a/span'
    #部门管理-新增
    dept_add = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-org/div/grid-action/div/div/div/button[1]'
    #部门管理-新增-机构名称
    dept_name = 'xpath=>//*[@id="name"]'
    # 部门管理-新增-备注
    dept_note = 'xpath=>//*[@id="comments"]'
    #部门管理-新增-保存
    dept_add_save = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[3]/button[2]'
    # 部门管理-修改
    dept_modify = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-org/div/grid-action/div/div/div/button[2]'
    # 部门管理-删除/修改-备注为测试备注001的记录
    dept_delete_info = 'xpath=>//div[text()="测试备注001"]'
    # 部门管理-删除
    dept_delete = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-org/div/grid-action/div/div/div/button[3]'
    #部门管理-删除-机构名称为开发部的记录
    dept_delete_info1 = 'xpath=>//div[text()="测试无法删除"]'

    #系统参数
    sys_para = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[1]/treeview-menu/ul/li[4]/a/span'
    #系统参数-短信平台设置
    sys_sms = 'xpath=>//tree-node-content/label/span[text()="短信平台设置"]'
    #系统参数-短信平台设置-短信签名
    sys_sms_set = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-parameters/div/div/div[2]/dynamic-form/form/div/div[3]/div/input'
    #保存
    sys_save = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-parameters/div/grid-action/div/div/div/button[2]'
    #确定
    sys_confirm = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[3]/button[2]'
    sys_result = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-parameters/div/div/div[2]'






