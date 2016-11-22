from selenium.webdriver.common.keys import Keys


class dispath_helper:
    def __init__(self, app):
        self.app = app

    def fill_dest_country(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_DdlCountries_I").clear()
        wd.find_element_by_id("PageControlPostingType_DdlCountries_I").send_keys("АЗЕРБАЙДЖАН")
        wd.find_element_by_id("PageControlPostingType_DdlCountries_I").send_keys(Keys.TAB)

    def fill_posting_type(self):
        wd = self.app.wd
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_DdlPostingKindsCategories_I")
