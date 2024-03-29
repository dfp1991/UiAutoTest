#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from pageobject.page.BasePage import BasePage
from pageobject.page.ProfilePage import ProfilePage
from pageobject.page.SearchPage import SearchPage
from pageobject.page.SelectedPage import SelectedPage
from pageobject.page.MarketQuotationsPage import MarketQuotationsPage





class MainPage(BasePage):
    _profile_button=(By.ID,"user_profile_icon")
    _search_button=(By.ID,"home_search")
    def gotoSelected(self):
        #调用全局的driver对象使用webdriver.api定位元素
        zixuan=(By.XPATH,"//*[@text='自选']")
        self.find(zixuan)
        self.find(zixuan).click()
        #self.driver.find_element(By.xpath, "//*[@text='自选']")
        #self.driver.find_element_by_xpath("//*[@text='自选']")
        #self.driver.find_element_by_xpath("//*[@text='自选']").click()
        return SelectedPage()

    def gotoMarketQuotations(self):
        hangqing=(By.XPATH,"//*[@text='行情']")
        self.find(hangqing)
        self.find(hangqing).click()
        return MarketQuotationsPage()

    def gotoSearch(self) ->SearchPage:
        self.find(self._search_button).click()
        return SearchPage()

    def gotoProfile(self):
        self.find(MainPage._profile_button).click()
        return ProfilePage()
