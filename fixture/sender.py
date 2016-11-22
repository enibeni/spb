from selenium.webdriver.common.keys import Keys


class sender_helper:
    def __init__(self, app):
        self.app = app

    def fill_kpp(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        wd.find_element_by_id("PageControlPostingType_FromKpp_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromKpp_I").send_keys("997250001")

    def fill_inn(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInn_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInn_I").send_keys("773605000312")

    def fill_home(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromHome_I").click()
        wd.find_element_by_id("PageControlPostingType_FromHome_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromHome_I").send_keys("5")
        wd.find_element_by_id("PageControlPostingType_FromHome_I").send_keys(Keys.TAB)
        self.app.is_alert_present(wd, True)

    def fill_street(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='Sender_Street']/select[1]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='Sender_Street']/select[1]//option[2]").click()

    def fill_city(self):
        wd = self.app.wd
        if not wd.find_element_by_xpath("//div[@id='Sender_City']/select[1]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='Sender_City']/select[1]//option[10]").click()

    def fill_region(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("select").click()
        if not wd.find_element_by_xpath("//div[@id='Sender_Region']/select[1]//option[47]").is_selected():
            wd.find_element_by_xpath("//div[@id='Sender_Region']/select[1]//option[47]").click()

    def fill_zipcode(self):
        wd = self.app.wd
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_FromZipCode_I")
        wd.find_element_by_id("PageControlPostingType_FromZipCode_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromZipCode_I").send_keys("111394")
        wd.find_element_by_id("SenderRegionWrap").click()
        self.app.is_alert_present(wd, True)
        self.app.wait_and_click_by_id(wd, "SenderRegionWrap")

    def fill_company_name(self):
        wd = self.app.wd
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_FromCompany_I")
        wd.find_element_by_id("PageControlPostingType_FromCompany_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCompany_I").send_keys("company")