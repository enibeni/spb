# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys


class dispath_helper:
    def __init__(self, app):
        self.app = app

    def fill_dest_country(self, country):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_DdlCountries_I").clear()
        wd.find_element_by_id("PageControlPostingType_DdlCountries_I").send_keys(country)
        wd.find_element_by_id("PageControlPostingType_DdlCountries_I").send_keys(Keys.TAB)

    def fill_posting_type(self, post_type):
        wd = self.app.wd
        if type == "Посылка":
            self.app.wait_and_click_by_id(wd, "PageControlPostingType_DdlPostingKindsCategories_I")

    def choose_blank_type(self, blank_type):
        wd = self.app.wd
        wd.find_element_by_id()
