# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_email_page()
        wd.implicitly_wait(5)
        wd.find_element(By.NAME, 'identifier').send_keys(username)
        wd.implicitly_wait(5)
        WebDriverWait(wd, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.VfPpkd-RLmnJb'))).click()
        WebDriverWait(wd, 20).until(EC.visibility_of_element_located((By.NAME, 'password'))).send_keys(password)
        wd.implicitly_wait(5)
        WebDriverWait(wd, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.VfPpkd-RLmnJb'))).click()

    def logout(self):
        wd = self.app.wd
        WebDriverWait(wd, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "gb_La gbii"))).click()
        WebDriverWait(wd, 20).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Выйти"]'))).click()
