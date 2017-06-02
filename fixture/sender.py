# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys


class sender_helper:
    def __init__(self, app):
        self.app = app

    def fill_kpp(self, kpp):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        wd.find_element_by_id("PageControlPostingType_FromKpp_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromKpp_I").send_keys(kpp)

    def fill_inn(self, inn):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInn_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInn_I").send_keys(inn)

    def fill_home(self, home):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromHome_I").click()
        wd.find_element_by_id("PageControlPostingType_FromHome_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromHome_I").send_keys(home)
        wd.find_element_by_id("PageControlPostingType_FromHome_I").send_keys(Keys.TAB)
        self.app.is_alert_present(wd, False)

    def fill_street(self, street):
        wd = self.app.wd
        wd.find_element_by_xpath(".// *[ @ id = 'Sender_Street'] / div[2] / input").click()
        wd.find_element_by_xpath(".// *[ @ id = 'Sender_Street'] / div[2] / input").send_keys(street)
        wd.find_element_by_xpath(".// *[ @ id = 'Sender_Street'] / div[2] / input").send_keys(Keys.TAB)
        self.app.is_alert_present(wd, False)

    def fill_city(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".// *[ @ id = 'Sender_City'] / div[2] / input").click()

    def fill_region(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("select").click()
        if not wd.find_element_by_xpath("//div[@id='Sender_Region']/select[1]//option[47]").is_selected():
            wd.find_element_by_xpath("//div[@id='Sender_Region']/select[1]//option[47]").click()

    def fill_zipcode(self, zip):
        wd = self.app.wd
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_FromZipCode_I")
        wd.find_element_by_id("PageControlPostingType_FromZipCode_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromZipCode_I").send_keys(zip)
        wd.find_element_by_id("SenderRegionWrap").click()
        self.app.is_alert_present(wd, True)
        self.app.wait_and_click_by_id(wd, "SenderRegionWrap")

    def fill_company_name(self, company_name):
        wd = self.app.wd
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_FromCompany_I")
        wd.find_element_by_id("PageControlPostingType_FromCompany_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCompany_I").send_keys(company_name)