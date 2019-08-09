#!/user/bin/env python
# -*- coding:utf-8 -*-

from pageobject.driver.AndroidClient import AndroidClient


class MarketQuotationsPage(object):

    def getPriceByName(self,name) ->float:
        #todo:
        price=AndroidClient.driver\
            .find_element_by_xpath("//*[contains(@resource-id,'index_name') and @text='"+name+"']"+
            "/..//*[contains(@resource-id,'index_price')]").text
        return float(price)
