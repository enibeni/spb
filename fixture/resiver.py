class reciver_helper:
    def __init__(self, app):
        self.app = app

    def fill_resiv_home(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_ToHome_I").click()
        wd.find_element_by_id("PageControlPostingType_ToHome_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToHome_I").send_keys("4")

    def fill_resiv_street(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_ToStreet_I").click()
        wd.find_element_by_id("PageControlPostingType_ToStreet_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToStreet_I").send_keys("улица")

    def fill_resiv_city(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_ToSettlement_I").click()
        wd.find_element_by_id("PageControlPostingType_ToSettlement_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToSettlement_I").send_keys("город")

    def fill_resiv_name(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").click()
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").send_keys("Иванов Иван Иванович")