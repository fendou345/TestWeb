# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuxuexue
@file: hos_manage.py
@time: 2018/04/08
"""

class PageHospital(object):
    """
    与医院管理有关元素
    """
    #医院管理
    hos_manage = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[2]/a'
    #医院信息
    hos_info = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[2]/treeview-menu/ul/li[1]/a/span'
    #医院信息-新增
    hos_add = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/grid-action/div/div/div/button[2]'
    #医院信息-新增-医院名称
    hos_name = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[1]/div[1]/div/input'
    # 医院信息-新增-联系方式
    hos_phone = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[1]/div[2]/div/input'
    # 医院信息-新增-省
    hos_add_province = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/app-select-area/div/div[1]/div/sui-select'
    #医院信息-新增-省-陕西省
    hos_add_province_shanxi = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/app-select-area/div/div[1]/div/sui-select/div[3]/sui-select-option[27]'
    # 医院信息-新增-市
    hos_add_city = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/app-select-area/div/div[2]/div/sui-select/div[1]'
    # 医院信息-新增-市-延安
    hos_add_city_yanan = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/app-select-area/div/div[2]/div/sui-select/div[3]/sui-select-option[6]'
    # 医院信息-新增-经度
    hos_longitude = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[2]/div[1]/div/input'
    # 医院信息-新增-纬度
    hos_latitude = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[2]/div[2]/div/input'
    #医院信息-新增-地址
    hos_address = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[3]/div[1]/div/input'
    # 医院信息-新增-邮箱
    hos_email = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[3]/div[2]/div/input'
    # 医院信息-新增-医院等级
    hos_add_level = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[4]/div[1]/div/sui-select'
    # 医院信息-新增-医院等级-三级乙等
    hos_add_level01 = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[4]/div[1]/div/sui-select/div[3]/sui-select-option[2]'
    # 医院信息-新增-状态
    hos_add_status = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[4]/div[2]/div/sui-select'
    # 医院信息-新增-状态-已上线
    hos_add_status01 = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[4]/div[2]/div/sui-select/div[3]/sui-select-option[1]'
    # 医院信息-新增-网址
    hos_url = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[5]/div[1]/div/input'
    # 医院信息-新增-邮编
    hos_postcode = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[5]/div[2]/div/input'
    # 医院信息-新增-端地址
    hos_portaddress = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[6]/div[1]/div/input'
    # 医院信息-新增-网络医院
    hos_air = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[6]/div[2]/div/sui-checkbox'
    # 医院信息-新增-LOGO
    hos_logo = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/app-file-upload/div/div/div/div/input'
    # 医院信息-新增-简介
    hos_introduction = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[7]/div/textarea'
    #医院信息-新增-确定
    hos_confirm = 'xpath=>//button[text()="确定"]'
    #医院信息-重置
    hos_reset = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/grid-action/div/div/div/button[4]'
    #医院信息-医院信息表格框
    hos_result = 'class_name=>demo-contents'
    # 医院信息-医院信息表格框向下滚动
    hos_js = "var q=document.getElementsByClassName('ag-body-viewport')[0].scrollTop=10000"
    #医院信息-末页
    hos_last_page = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/app-base-grid/div/div[2]/app-grid-bbar/nav/form/button[4]'
    # 医院信息-修改
    hos_modify = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/grid-action/div/div/div/button[3]'
    # 医院信息-修改-最后一个医院
    hos_id = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div'
    # 医院信息-查询
    hos_query = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/grid-action/div/div/div/button[1]'
    #医院信息-查询-医院名称
    hos_query_name = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/div/div/div[1]/div/input'
    #医院信息-查询-查询结果-医院名称
    hos_query_name_result = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[2]'
    #医院信息-状态
    hos_status = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/div/div/div[2]/div/sui-select'
    #医院信息-状态-已上线
    hos_status01 = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/div/div/div[2]/div/sui-select/div[3]/sui-select-option[1]'
    #医院信息-查询结果-已上线
    hos_query_status_result = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[5]'
    #医院信息-显示条数每页
    hos_show_num = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/app-base-grid/div/div[2]/app-grid-bbar/nav/div/sui-select[2]'
    # 医院信息-显示条数每页(10页)
    hos_show_num01 = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/app-base-grid/div/div[2]/app-grid-bbar/nav/div/sui-select[2]/div[2]/sui-select-option[2]'
    # 医院信息-下一页
    hos_next_page = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/app-base-grid/div/div[2]/app-grid-bbar/nav/form/button[3]'
    # 医院信息-省
    hos_province = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/div/app-select-area/div/div[1]/div/sui-select'
    # 医院信息-省-陕西省
    hos_province_shanxi = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/div/app-select-area/div/div[1]/div/sui-select/div[3]/sui-select-option[27]'
    #医院信息-市
    hos_city = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/div/app-select-area/div/div[2]/div/sui-select'
    #医院信息-市-延安
    hos_city_yanan = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-hospital-infor/div/app-select-area/div/div[2]/div/sui-select/div[3]/sui-select-option[6]'
    #医院信息-省
    hos_province_text = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/app-select-area/div/div[1]/div/sui-select/div[1]'
    #医院信息-市
    hos_city_text = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/app-select-area/div/div[2]/div/sui-select/div[1]'
    # 医院信息-状态
    hos_status_text = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[4]/div[2]/div/sui-select/div[1]'
    #医院信息-取消
    hos_cancel = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[3]/button[1]'

    #科室信息
    dept_info = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[2]/treeview-menu/ul/li[2]/a/span'
    #科室信息-省
    dept_province = 'xpath=>//app-select-area/div/div[1]/div/sui-select'
    # 科室信息-省-陕西省
    dept_province_shanxi = 'xpath=>//app-select-area/div/div[1]/div/sui-select/div[3]/sui-select-option[27]'
    #科室信息-市
    dept_city = 'xpath=>//app-select-area/div/div[2]/div/sui-select'
    #科室信息-市-西安市
    dept_city_xian = 'xpath=>//app-select-area/div/div[2]/div/sui-select/div[3]/sui-select-option[1]'
    #科室信息-等级
    dept_level = 'xpath=>//div[1]/div/div[1]/div/sui-select'
    #科室信息-等级-三级甲等
    dept_level01 = 'xpath=>//div[1]/div/div[1]/div/sui-select/div[3]/sui-select-option[1]'
    # 科室信息-医院
    dept_hos = 'xpath=>//div[1]/div/div[2]/div/sui-select'
    # 科室信息-医院-西安交通大学第一附属医院
    dept_hos01 = 'xpath=>//div[1]/div/div[2]/div/sui-select/div[3]/sui-select-option[1]'
    #科室信息-新增
    dept_add = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[1]'
    # 科室信息-修改
    dept_modify = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[2]'
    # 科室信息-删除
    dept_delete = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[3]'
    # 科室信息-导诊科室维护
    dept_guide = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[4]'
    # 科室信息-重置
    dept_reset = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[5]'
    #选择一级科室-五官科
    dept_test = 'xpath=>//tree-node-content/label/span[text()="五官科"]'
    #选择二级科室-麻醉科
    dept_test01 = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div'
    #科室信息-新增-确定
    dept_add_confirm = 'xpath=>//div/button[text()="确定"]'
    #科室信息-二级科室名
    dept_deptname = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[2]'
    #科室信息修改-科室简介
    dept_introduction = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/form/div[2]/div[2]/div/textarea'
    #科室信息-导诊维护-一级科室展开按钮
    dept_guide_expand = 'xpath=>//*[@id="tree_56"]/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node[1]/div/tree-node-wrapper/div/tree-node-expander/span/span'
    # 科室信息-导诊维护-二级科室
    dept_guide_dept = 'xpath=>//tree-node-collection/div/tree-node[7]/div/tree-node-wrapper/div/div/tree-node-content/label/span[text()="血管外科"]'
    #科室信息-导诊科室名
    dept_guidename = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[3]'
    #一级科室对应的二级科室数据
    dept_result = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div'

    #医生信息
    doc_info = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[2]/treeview-menu/ul/li[3]/a/span'
    #医生信息-重置
    doc_reset = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-doctor-infor/grid-action/div/div/div/div[1]/button[2]'
    # 医生信息-详情
    doc_detail = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-doctor-infor/grid-action/div/div/div/div[1]/button[1]'
    # 医生信息-查询
    doc_query = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-doctor-infor/grid-action/div/div/div/div[2]/div/input'
    #医生信息-内科室收缩按钮
    doc_expand = 'xpath=>//tree-node[1]/div/tree-node-wrapper/div/tree-node-expander/span/span[@class="toggle-children"]'
    #医生信息-测试科室展开按钮
    doc_expand_test = 'xpath=>//tree-node[10]/div/tree-node-wrapper/div/tree-node-expander/span/span[@class="toggle-children"]'
    #医生信息-测试科室
    doc_dept = 'xpath=>//tree-node/div/tree-node-wrapper/div/div/tree-node-content/label/span[text()="测试科室"]'
    #医生信息-具体医生
    doc_info_detail = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[1]/div/div[1]'
    #医生信息-详情-上传图片
    doc_image = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[1]/app-file-upload/div/div/div/div/input'
    # 医生信息-详情-关闭
    doc_close = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[2]/button'
    #医生信息-医生名字
    doc_name = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[3]'

    #互联网医院排班
    schedu = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[2]/treeview-menu/ul/li[4]/a/span'
    #新增排班
    schedu_add = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-air-hospital-schedule/grid-action/div/div/div/button'
    #平均问诊时间
    avg_time = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[2]/input'
    #平均问诊时间-更新
    avg_time_update = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[2]/button'
    #挂号类型
    registered_type = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[3]/div[1]/div[1]/sui-select'
    # 挂号类型-普通号
    registered_type01 = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[3]/div[1]/div[1]/sui-select/div[2]/sui-select-option[1]'
    # 上下午
    time = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[3]/div[1]/div[2]/sui-select'
    #上午
    time_am = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[3]/div[1]/div[2]/sui-select/div[2]/sui-select-option[1]'
    #下午
    time_pm = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[3]/div[1]/div[2]/sui-select/div[2]/sui-select-option[2]'
    #保存
    schedu_save = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[2]/div/button[1]'
    #医生
    schedu_doc = 'xpath=>//app-add-air-hospital-schedule/div[3]/div[1]/div[3]/div/ul/li[1]/span'
    schedu_doc01= 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-add-air-hospital-schedule/div[3]/div[1]/div[3]/div/ul/li[1]/span/strong[text()="sw10020"]'
    #日期
    schedu_time_today = 'xpath=>//mwl-calendar-week-view-header/div/div[contains(@class, "cal-today")]'
    schedu_time_tomorrow01 = 'xpath=>//mwl-calendar-week-view/div/mwl-calendar-week-view-header/div/div/b[text()="星期日"]'
    schedu_time_tomorrow02 = 'xpath=>//mwl-calendar-week-view-header/div/div[contains(@class, "cal-today")]/./following-sibling::div[1]'
    #下一个
    next_week = '//mwl-demo-utils-calendar-header/div/div[1]/div/div[3]'
    #医院排班列表
    save_result = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-air-hospital-schedule/div[2]/div[2]/div[2]/mwl-calendar-week-view/div/div'
    #删除
    schedu_delete = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-air-hospital-schedule/div[2]/div[2]/div[2]/mwl-calendar-week-view/div/div/div[1]/mwl-calendar-week-view-event/div/mwl-calendar-event-title/a/div/i'
    #删除确认
    schedu_delete_confirm = 'xpath=>/html/body/app-root/jaspero-confirmations/jaspero-confirmation/div[2]/div[3]/button[2]'

    #科室挂号费
    deptprice = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/sidebar-menu/div[2]/ul/li[2]/treeview-menu/ul/li[5]/a/span'
    #科室挂号费-新增
    price_add = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[1]'
    # 科室挂号费-修改
    price_modify = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[2]'
    # 科室挂号费-删除
    price_delete = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[3]'
    # 科室挂号费-重置
    price_reset = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/section/app-department-infor/grid-action/div/div/div/button[4]'
    #二级科室=体检科
    price_dept = 'xpath=>//tree-node-children/div/tree-node-collection/div/tree-node[4]/div/tree-node-wrapper/div/div/tree-node-content/label/span[text()="体检科"]'
    #门诊类型（普通号）
    treat_type = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[2]/form/div/div[1]/div/sui-select'
    treat_type01 = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[2]/form/div/div[1]/div/sui-select/div[3]/sui-select-option[1]'
    #价格
    price = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[2]/form/div/div[2]/div/div/input'
    #确定
    price_confirm = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[3]/button[2]'
    #二级科室下号源类型列表
    price_result = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div'
    #选择号源类型
    price_info = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[text()="专家号"]'
    price_info01 = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[text()="普通号"]'
    #专家号号源价格
    price_info_price = 'xpath=>//*[@id="borderLayout_eGridPanel"]/div[1]/div/div[4]/div[3]/div/div/div/div[text()="专家号"]/./following-sibling::div[1]'
    #删除确定
    price_delete_confirm = 'xpath=>/html/body/app-root/jaspero-confirmations/jaspero-confirmation/div[2]/div[3]/button[2]'