#!/user/bin/env python
# -*- coding:utf-8 -*-

import pytest
from pageobject.page.MainPage import MainPage

class TestMarketQuotations(object):
    def test_price(self):
        main=MainPage()
        assert main.gotoMarketQuotations().getPriceByName("深证成指") > 8000