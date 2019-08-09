#!/user/bin/env python
# -*- coding:utf-8 -*-
from pageobject.driver.AndroidClient import AndroidClient


class SelectedPage(object):
    def addDefault(self):
        return self

    def getPriceByName(self,name) ->float:
        #todo:
        price=AndroidClient.driver\
            .find_element_by_xpath("//*[contains(@resource-id,'stockName') and @text='"+name+"']"+
            "/../../../..//*[contains(@resource-id,'currentPrice')]").text
        return float(price)
