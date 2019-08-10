#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from pageobject.page.BasePage import BasePage


class MarketQuotationsPage(BasePage):

    def getPriceByName(self,name) ->float:
        priceLocator=(By.XPATH,"//*[contains(@resource-id,'index_name') and @text='"+name+"']"+
            "/..//*[contains(@resource-id,'index_price')]")
        price=self.find(priceLocator).text
        return float(price)
