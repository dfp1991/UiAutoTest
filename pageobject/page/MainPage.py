#!/user/bin/env python
# -*- coding:utf-8 -*-
from pageobject.driver.AndroidClient import AndroidClient
from pageobject.page.SelectedPage import SelectedPage
from pageobject.page.MarketQuotationsPage import MarketQuotationsPage

class MainPage(object):
    def __init__(self):
        AndroidClient.restart_app()

    def gotoSelected(self):
        #调用全局的driver对象使用webdriver.api定位元素
        AndroidClient.driver.find_element_by_xpath("//*[@text='自选']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='自选']").click()
        return SelectedPage()

    def gotoMarketQuotations(self):
        AndroidClient.driver.find_element_by_xpath("//*[@text='行情']")
        AndroidClient.driver.find_element_by_xpath("//*[@text='行情']").click()
        return MarketQuotationsPage()
