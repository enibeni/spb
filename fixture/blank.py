class blank_helper:
    def __init__(self, app):
        self.app = app

    def fill_period(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").click()
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").send_keys("30")

    def fill_note(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").click()
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").send_keys("примечание")

    def fill_cur_post_number(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").send_keys("12345")

    def fill_parse_number(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").send_keys("12345")

    def fill_currancy(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_DdlCurrencyOnDelivery_B-1").click()
        self.app.wait_and_click_by_id(wd, "PageControlPostingType_DdlCurrencyOnDelivery_DDD_L_LBI115T0")

    def fill_cash_on_delivery(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").send_keys("100")

    def fill_declaired_value(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").click()
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").send_keys("1000")

    def fill_imp_invoice2(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").send_keys("12345")

    def fill_imp_invoice(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").send_keys("12345")

    def fill_imp_cert2(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").send_keys("12345")

    def fill_imp_cert(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").send_keys("12345")

    def fill_imp_licence2(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").send_keys("12345")

    def fill_imp_license(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").click()
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").send_keys("12345")

    def fill_imp_email(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").send_keys("qqq@qq.ru")

    def fill_imp_fax(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").send_keys("111111")

    def fill_imp_phone(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").send_keys("111111")

    def fill_imp_requisities(self):
        wd = self.app.wd
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").send_keys("111111")

    def fill_dispatch(self):
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