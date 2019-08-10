#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from pageobject.page.BasePage import BasePage

class SelectedPage(BasePage):
    def addDefault(self):
        return self

    def getPriceByName(self,name) ->float:
        priceLocator=(By.XPATH,"//*[contains(@resource-id,'stockName') and @text='"+name+"']"+
            "/../../../..//*[contains(@resource-id,'currentPrice')]")
        price=self.find(priceLocator).text
        return float(price)
