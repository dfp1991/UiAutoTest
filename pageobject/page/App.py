#!/user/bin/env python
# -*- coding:utf-8 -*-
from pageobject.driver.AndroidClient import AndroidClient
from pageobject.page.BasePage import BasePage
from pageobject.page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.getClient().restart_app()
        return MainPage()