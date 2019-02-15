# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:liuxuexue
@file: test_login.py
@time: 2018/04/08
"""

class PageLogin(object):
    """
    与登录有关元素
    """
    # 用户名
    user='css_selector=>#username'
    # 密码
    pwd='css_selector=>#password'
    #登录
    login = 'xpath=>/html/body/app-root/login/div/div[1]/div/div[1]/form/div[3]/button'
    # 忘记密码
    forpwd='class_name=>text-primary'
    # 忘记密码——>手机号
    phonenum ='css_selector=>#phone'
    # 忘记密码——>获取验证码
    verification ='xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[2]/div[2]/div[1]/form/div[2]/div[3]/button'
    #忘记密码——>输入验证码
    veri_num = 'css_selector=>#code'
    #忘记密码——>下一步
    next = 'xpath=>/html/body/sui-modal/sui-dimmer/div/div/div/div[2]/div[2]/div[1]/form/div[3]/button'
    #登录后——>title
    title = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/ng-sidebar/aside/div/nav/h5'
    #登录后——>用户名
    user_button = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/nav/div/form[6]/ul/li/a'
    #登录后——>退出
    user_quit = 'xpath=>/html/body/app-root/ng-component/ng-sidebar-container/div/div/nav/div/form[6]/ul/li/ul/li[6]/a'
    #登录后——>退出——>确认
    confirm = 'css_selector=>body > ngb-modal-window > div > div > confirm > div > div.text-center.c-mb20.c-mt10 > button.btn.btn-primary'
    #退出后——>登录
    login_title = 'class_name=>c-login-title'
    #密码不正确&验证码错误
    message = "xpath=>/html/body/app-root/toast-box/div/div/toast/div/strong"





