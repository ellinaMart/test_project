# -*- coding: utf-8 -*-
import json
import os
from .testdata import test_data
import allure
import pytest


@pytest.mark.parametrize('letter', test_data, ids=[repr(x) for x in test_data])
@allure.feature('News')
def test_send_email(app, letter):
    with allure.step("пишем письмо и отправляем"):
        app.write_letter(letter)
        app.go_to_sent_letters()

    with allure.step("получаем список всех отправленных писем"):
        app.get_email_list()
        list_of_email = app.get_email_list()

    with allure.step("проверяем, что наше письмо есть в списке отправленных"):
        assert letter.email_subject in list_of_email
    








    #app.session.logout()
