#!/user/bin/env python
# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.page.BasePage import BasePage
from selenium.webdriver.support import expected_conditions


class ProfilePage(BasePage):
    _rl_login_phone=(By.ID,"rl_login_phone")
    _rl_login_wx=(By.ID,"rl_login_wx")
    _register_phone_number=(By.ID,"register_phone_number")
    _register_code=(By.ID,"register_code")
    _tv_login_with_account=(By.ID,"tv_login_with_account")
    _login_account=(By.ID,"login_account")
    _login_password=(By.ID,"login_password")
    _button_next=(By.ID,"button_next")
    _iv_action_back=(By.ID,"iv_action_back")
    _md_buttonDefaultNegative=(By.ID,"md_buttonDefaultNegative")
    _error_msg=(By.ID,"md_content")


    def loginByWX(self):
        return self

    def loginByMSG(self,phone,code):
        return self

    def loginByPassword(self,account,password):
        self.find(self._rl_login_phone).click()
        self.find(self._tv_login_with_account).click()
        self.find(self._login_account).send_keys(account)
        self.find(self._login_password).send_keys(password)
        self.find(self._button_next).click()
        return self

    def loginSuccessByPassword(self, account, password):
        from pageobject.page.MainPage import MainPage
        return MainPage()

    def back(self):
        #WebDriverWait(self.driver,2).until(expected_conditions.presence_of_element_located(self._iv_action_back))
        self.find(self._iv_action_back).click()
        self.find(self._md_buttonDefaultNegative).click()
        return self

    def getErrorMsg(self):
        msg=self.find(self._error_msg).text
        self.findByText("确定").click()
        return msg



