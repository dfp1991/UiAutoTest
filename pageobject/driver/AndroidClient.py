#!/user/bin/env python
# -*- coding:utf-8 -*-
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AndroidClient(object):
    driver=WebDriver

    @classmethod
    def install_app(cls) ->WebDriver:
        caps = {}
        #如果有必要，进行第一次安装
        caps["platformName"] = "android"
        caps["deviceName"] = "dfp"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #解决第一次启动的问题
        caps["autoGrantPermission"] = "true"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        #4723
        cls.driver.implicitly_wait(10)
        return cls.driver

    @classmethod
    def restart_app(cls) ->WebDriver:
        caps = {}
        #如果有必要，进行第一次安装
        caps["platformName"] = "android"
        caps["deviceName"] = "dfp"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        #为了更快的启动，并保留之前的数据，从而可以保存上一个case执行后的状态
        caps["noReset"] = True
        caps["chromedriverExecutableDir"] = "/User/seveniruby/projects/chromedriver/2.20"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
        cls.driver.implicitly_wait(10)
        return cls.driver
