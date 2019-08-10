#!/user/bin/env python
# -*- coding:utf-8 -*-
from appium.webdriver import WebElement
from selenium.webdriver.common.by import By

from pageobject.driver.AndroidClient import AndroidClient


class BasePage(object):
    def __init__(self):
        self.driver=AndroidClient.driver

    def find(self, kv) ->WebElement:
        return self.driver.find_element(*kv)

    def findByText(self,text):
        return self.find((By.XPATH,"//*[@text='%s']" %text))
