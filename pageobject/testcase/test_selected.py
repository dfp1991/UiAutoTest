#!/user/bin/env python
# -*- coding:utf-8 -*-

import pytest
from pageobject.page.App import App
from pageobject.page.MainPage import MainPage

class TestSelected(object):
    @classmethod
    def setup_class(cls):
        cls.mainPage=App.main()

    def test_price(self):
        assert self.mainPage.gotoSelected().getPriceByName("苹果") > 100


