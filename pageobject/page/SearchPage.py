#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By

from pageobject.page.BasePage import BasePage


class SearchPage(BasePage):
    _edit_locator=(By.CLASS_NAME, "android.widget.EditText")

    def search(self,key):
        self.find(self._edit_locator).send_keys(key)
        return self

    def addToSelected(self,key):
        self.find(key).click()
        return self

    def isInSelected(self,key):
        follow_button=(By.XPATH,"//*[contains(@resource-id,'stockCode') and contains(@text,'%s')]/../../.."%key+
                                "//*[contains(@resource-id,'follow')]")
        id=self.find(follow_button).get_attribute("resourceId")
        print(id)
        return "followed_btn" in id

    def searcByUser(self, key):
        pass

    def isFollowed(self):
        pass

