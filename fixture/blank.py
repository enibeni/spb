# -*- coding: utf-8 -*-

from selenium.webdriver.common.keys import Keys

class blank_helper:
    def __init__(self, app):
        self.app = app

    def fill_period(self, period):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").click()
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").send_keys(period)

    def fill_note(self, note):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").click()
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").send_keys(note)

    def fill_cur_post_number(self, cur_post_number):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").send_keys(cur_post_number)

    def fill_parse_number(self, parse_number):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").send_keys(parse_number)

    def fill_currancy(self, currancy):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_DdlCurrencyOnDelivery_I").click()
        wd.find_element_by_id("PageControlPostingType_DdlCurrencyOnDelivery_I").clear()
        wd.find_element_by_id("PageControlPostingType_DdlCurrencyOnDelivery_I").send_keys(currancy)
        wd.find_element_by_id("PageControlPostingType_DdlCurrencyOnDelivery_I").send_keys(Keys.TAB)
        # self.app.wait_and_click_by_id(wd, "PageControlPostingType_DdlCurrencyOnDelivery_DDD_L_LBI115T0")

    def fill_cash_on_delivery(self, cash_on_delivery):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").send_keys(cash_on_delivery)

    def fill_declaired_value(self, declaired_value):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").click()
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").send_keys(declaired_value)

    def fill_invoice2(self, invoice2):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").send_keys(invoice2)

    def fill_invoice(self, invoice):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").send_keys(invoice)

    def fill_cert2(self, cert2):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").send_keys(cert2)

    def fill_cert(self, cert):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").send_keys(cert)

    def fill_licence2(self, licence2):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").send_keys(licence2)

    def fill_licence(self, licence):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").click()
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").send_keys(licence)

    def fill_email(self, email):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").send_keys(email)

    def fill_fax(self, fax):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").send_keys(fax)

    def fill_phone(self, phone):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").send_keys(phone)

    def fill_requisities(self, requisities):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").send_keys(requisities)

    def fill_attachs(self):
        wd = self.app.wd
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_AttachName0_I")
        wd.find_element_by_id("PageControlPostingType_AttachName0_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachName0_I").send_keys("Рубашка х/б")
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_AttachCount0_I")
        wd.find_element_by_id("PageControlPostingType_AttachCount0_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachCount0_I").send_keys("1")
        wd.find_element_by_id("PageControlPostingType_AttachWeight0_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachWeight0_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachWeight0_I").send_keys("1")
        wd.find_element_by_id("PageControlPostingType_AttachCost0_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachCost0_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachCost0_I").send_keys("1000")
        wd.find_element_by_id("PageControlPostingType_AttachTNVED0_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachTNVED0_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachTNVED0_I").send_keys("6105100000")
        wd.find_element_by_id("PageControlPostingType_AttachCountry0_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachCountry0_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachCountry0_I").send_keys("АВСТРИЯ")