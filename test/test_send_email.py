# -*- coding: utf-8 -*-
import json
import os
import pytest
from .testdata import test_data

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..',  'config.json')) as config_file:
    config = json.load(config_file)

#@pytest.mark.parametrize('letter', test_data)
def test_send_email(app):
    #открываем начальную страницу
    app.open_email_page()
    #авторизуемся в почте
    app.session.login(username=config["username"], password=config["password"])
    #пишем письмо
    app.write_letter(test_data)
    #и отправляем
    app.go_to_sent_letters()
    #получаем список всех отправленных писем
    app.get_email_list()
    list_of_email = app.get_email_list()
    #проверяем, что наше письмо есть в списке отправленных
    assert test_data.email_subject in list_of_email
    








    #app.session.logout()
