#!/user/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from pageobject.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver=self.getDriver()

    @classmethod
    def getDriver(cls):
        cls.driver=AndroidClient.driver
        return cls.driver

    @classmethod
    def getClient(cls):
        return AndroidClient


    def find(self, kv) ->WebElement:
        #todo:处理各类弹框
        return self.driver.find_element(*kv)

    def findByText(self,text):
        return self.find((By.XPATH,"//*[@text='%s']" %text))
