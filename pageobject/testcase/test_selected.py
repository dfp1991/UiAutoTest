#!/user/bin/env python
# -*- coding:utf-8 -*-

import pytest

from pageobject.page.App import App

class TestSelected(object):
    def test_price(self):
        main=App.main()
        assert main.gotoSelected().getPriceByName("苹果") > 200

    def test_is_selected_stock(self):
        searchPage=App.main().gotoSearch().search("alibaba")
        assert searchPage.isInSelected("BABA")==True
        assert searchPage.isInSelected("1688")==False

    def test_is_follow_user(self):
        pass

