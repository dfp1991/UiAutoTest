#!/user/bin/env python
# -*- coding:utf-8 -*-
from pageobject.driver.AndroidClient import AndroidClient
from pageobject.page.MainPage import MainPage


class App(object):
    @classmethod
    def main(self):
        AndroidClient.restart_app()
        return MainPage()