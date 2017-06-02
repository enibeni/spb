# -*- coding: utf-8 -*-

class attach_helper:
    def __init__(self, app):
        self.app = app

    def fill_attachs(self, attachs):
        wd = self.app.wd
        i = 0
        print("%%%%%%%%%%%%%%%%%%%%%" + str(type(attachs)))
        for attach in attachs.attachs:
            print("!!!!!!!" + str(type(attachs)))
            self.app.wait_and_click_by_id(wd, "PageControlPostingType_AttachName" + str(i) + "_I")
            wd.find_element_by_id("PageControlPostingType_AttachName" + str(i) + "_I").clear()
            wd.find_element_by_id("PageControlPostingType_AttachName" + str(i) + "_I").send_keys(attach.attach_name)
            self.app.wait_and_click_by_id(wd, "PageControlPostingType_AttachCount" + str(i) + "_I")
            wd.find_element_by_id("PageControlPostingType_AttachCount" + str(i) + "_I").clear()
            wd.find_element_by_id("PageControlPostingType_AttachCount" + str(i) + "_I").send_keys(attach.count)
            wd.find_element_by_id("PageControlPostingType_AttachWeight" + str(i) + "_I").click()
            wd.find_element_by_id("PageControlPostingType_AttachWeight" + str(i) + "_I").clear()
            wd.find_element_by_id("PageControlPostingType_AttachWeight" + str(i) + "_I").send_keys(attach.weight)
            wd.find_element_by_id("PageControlPostingType_AttachCost" + str(i) + "_I").click()
            wd.find_element_by_id("PageControlPostingType_AttachCost" + str(i) + "_I").clear()
            wd.find_element_by_id("PageControlPostingType_AttachCost" + str(i) + "_I").send_keys(attach.cost)
            wd.find_element_by_id("PageControlPostingType_AttachTNVED" + str(i) + "_I").click()
            wd.find_element_by_id("PageControlPostingType_AttachTNVED" + str(i) + "_I").clear()
            wd.find_element_by_id("PageControlPostingType_AttachTNVED" + str(i) + "_I").send_keys(attach.TNVED)
            wd.find_element_by_id("PageControlPostingType_AttachCountry" + str(i) + "_I").click()
            wd.find_element_by_id("PageControlPostingType_AttachCountry" + str(i) + "_I").clear()
            wd.find_element_by_id("PageControlPostingType_AttachCountry" + str(i) + "_I").send_keys(attach.country)
            i += 1

    def fill_attach(self, attach_name, count, weight, cost, TNVED, country):
        wd = self.app.wd
        i = 0
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_AttachName" + str(i) + "_I")
        wd.find_element_by_id("PageControlPostingType_AttachName" + str(i) + "_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachName" + str(i) + "_I").send_keys(attach_name)
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_AttachCount" + str(i) + "_I")
        wd.find_element_by_id("PageControlPostingType_AttachCount" + str(i) + "_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachCount" + str(i) + "_I").send_keys(count)
        wd.find_element_by_id("PageControlPostingType_AttachWeight" + str(i) + "_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachWeight" + str(i) + "_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachWeight" + str(i) + "_I").send_keys(weight)
        wd.find_element_by_id("PageControlPostingType_AttachCost" + str(i) + "_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachCost" + str(i) + "_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachCost" + str(i) + "_I").send_keys(cost)
        wd.find_element_by_id("PageControlPostingType_AttachTNVED" + str(i) + "_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachTNVED" + str(i) + "_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachTNVED" + str(i) + "_I").send_keys(TNVED)
        wd.find_element_by_id("PageControlPostingType_AttachCountry" + str(i) + "_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachCountry" + str(i) + "_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachCountry" + str(i) + "_I").send_keys(country)
