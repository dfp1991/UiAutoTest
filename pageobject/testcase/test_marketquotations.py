#!/user/bin/env python
# -*- coding:utf-8 -*-

import pytest
from pageobject.page.App import App

class TestMarketQuotations(object):
    def test_price(self):
        main=App.main()
        assert main.gotoMarketQuotations().getPriceByName("深证成指") > 8000