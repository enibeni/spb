# -*- coding: utf-8 -*-

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from fixture.dispatch import dispath_helper
from fixture.sender import sender_helper
from fixture.resiver import reciver_helper
from fixture.blank import blank_helper
from fixture.attach import attach_helper

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Application:
    def __init__(self):
        self.dispatch = dispath_helper(self)
        self.sender = sender_helper(self)
        self.reciver = reciver_helper(self)
        self.blank = blank_helper(self)
        self.attach = attach_helper(self)

        self.fp = webdriver.FirefoxProfile()
        self.fp.set_preference("browser.download.folderList", 2)
        self.fp.set_preference("browser.download.manager.showWhenStarting", False)
        self.fp.set_preference("browser.download.dir", ROOT_DIR)
        self.fp.set_preference("browser.download.manager.showWhenStarting", False)
        self.fp.set_preference("browser.download.manager.focusWhenStarting", False)
        self.fp.set_preference("browser.download.useDownloadDir", True)
        self.fp.set_preference("browser.helperApps.alwaysAsk.force", False)
        self.fp.set_preference("browser.download.manager.alertOnEXEOpen", False)
        self.fp.set_preference("browser.download.manager.closeWhenDone", True)
        self.fp.set_preference("browser.download.manager.showAlertOnComplete", False)
        self.fp.set_preference("browser.download.manager.useWindow", False)
        self.fp.set_preference("services.sync.prefs.sync.browser.download.manager.showWhenStarting", False)
        self.fp.set_preference("pdfjs.disabled", True)
        self.fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        self.fp.set_preference("http.response.timeout", 5)
        self.fp.set_preference("dom.max_script_run_time", 5)
        self.wd = webdriver.Firefox(firefox_profile=self.fp)

    def form_blank(self):
        wd = self.wd
        self.wait_and_click_by_id(self.wd, "PageControlPostingType_ASPxButton2_CD")
        self.is_alert_present(self.wd, True)
        self.is_alert_present(self.wd, False)

    def go_to_third_form(self):
        wd = self.wd
        wd.find_element_by_id("FillFormButton2").click()

    def go_to_second_form(self):
        wd = self.wd
        self.wait_and_click_by_id(self.wd, "FillFormButton")

    def open_home_page(self):
        wd = self.wd
        wd.get("http://10.3.1.8:8897/FillForm.aspx")

    def destroy(self):
        self.wd.quit()


    def is_alert_present(self, wd, accept):
        try:
            if accept:
                wd.switch_to.alert.accept()
            else:
                wd.switch_to.alert.dismiss()
            return True
        except:
            return False


    def wait_and_click_by_id(self, wd, web_element):
        wait = WebDriverWait(wd, 10)
        while True:
            try:
                element = wait.until(
                    EC.element_to_be_clickable((By.ID, web_element)))
                element.click()
                break
            except Exception as e:
                print(e)
