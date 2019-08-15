#!/user/bin/env python
# -*- coding:utf-8 -*-
from pageobject.page.App import App
import pytest


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage=App.main().gotoProfile()
    def setup_method(self):
        pass

    @pytest.mark.parametrize("user,pw,msg",[
        ("187681952781","111111","手机号码"),
        ("18768195278", "111111","密码错误")
    ])

    def test_login_password(self,user,pw,msg):
        self.profilePage.loginByPassword(user,pw)
        assert msg in self.profilePage.getErrorMsg()

    def teardown_method(self):
        self.profilePage.back()