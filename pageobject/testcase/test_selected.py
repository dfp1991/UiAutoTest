#!/user/bin/env python
# -*- coding:utf-8 -*-

import pytest
from pageobject.page.MainPage import MainPage

class TestSelected(object):
    def test_price(self):
        main=MainPage()
        assert main.gotoSelected().getPriceByName("苹果") > 213.04

    def test_add_stock(self):
        pass

