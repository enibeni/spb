# -*- coding: utf-8 -*-
import os

from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from os.path import expanduser

home = expanduser("~")
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def is_alert_present(wd, accept):
    try:
        if accept:
            wd.switch_to.alert.accept()
        else:
            wd.switch_to.alert.dismiss()
        return True
    except:
        return False


class test_spb(unittest.TestCase):
    def setUp(self):
        # self.wd = webdriver.Firefox()
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
        self.browser = webdriver.Firefox(firefox_profile=self.fp)
        # self.wd.implicitly_wait(60)


    def test_test_spb(self):
        success = True
        wd = self.browser

        wd.get("http://10.3.1.8:8897/FillForm.aspx")
        wd.find_element_by_id("PageControlPostingType_DdlCountries_B-1").click()
        time.sleep(float(4000) / 4000)
        ActionChains(wd).move_to_element(
            wd.find_element_by_id("PageControlPostingType_DdlCountries_DDD_L_LBI1T0")).perform()
        wd.find_element_by_id("PageControlPostingType_DdlCountries_DDD_L_LBI1T0").click()
        time.sleep(float(4000) / 4000)
        wd.find_element_by_id("PageControlPostingType_DdlPostingKindsCategories_B-1").click()
        ActionChains(wd).move_to_element(
            wd.find_element_by_id("PageControlPostingType_DdlPostingKindsCategories_DDD_L_LBI3T0")).perform()
        wd.find_element_by_id("PageControlPostingType_DdlPostingKindsCategories_DDD_L_LBI3T0").click()
        wd.find_element_by_id("FillFormButton").click()
        time.sleep(float(2000) / 2000)
        wd.find_element_by_id("PageControlPostingType_FromCompany_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCompany_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCompany_I").send_keys("company")
        time.sleep(float(2000) / 2000)
        # wd.find_element_by_id("PageControlPostingType_FromCountry_I").click()
        # wd.find_element_by_id("PageControlPostingType_FromCountry_I").send_keys("\\9")
        wd.find_element_by_id("PageControlPostingType_FromZipCode_I").click()
        wd.find_element_by_id("PageControlPostingType_FromZipCode_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromZipCode_I").send_keys("111394")
        wd.find_element_by_id("SenderRegionWrap").click()
        is_alert_present(self.browser, True)
        # try:
        #     wd.find_element_by_id("SenderRegionWrap").click()
        # except Exception:
        #     time.sleep(float(2000) / 2000)
        #     alert = wd.switch_to.alert
        #     alert.accept()
        # time.sleep(float(2000) / 2000)
        time.sleep(float(2000) / 2000)
        wd.find_element_by_id("SenderRegionWrap").click()
        time.sleep(float(2000) / 2000)
        wd.find_element_by_css_selector("select").click()
        if not wd.find_element_by_xpath("//div[@id='Sender_Region']/select[1]//option[47]").is_selected():
            wd.find_element_by_xpath("//div[@id='Sender_Region']/select[1]//option[47]").click()
        # wd.find_element_by_id().click()
        if not wd.find_element_by_xpath("//div[@id='Sender_City']/select[1]//option[10]").is_selected():
            wd.find_element_by_xpath("//div[@id='Sender_City']/select[1]//option[10]").click()
        if not wd.find_element_by_xpath("//div[@id='Sender_Street']/select[1]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='Sender_Street']/select[1]//option[2]").click()
        wd.find_element_by_id("PageControlPostingType_FromHome_I").click()
        wd.find_element_by_id("PageControlPostingType_FromHome_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromHome_I").send_keys("5")

        # wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        # try:
        #     wd.find_element_by_id("PageControlPostingType_FromHome_I").send_keys("5")
        #     wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        #     wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        # except Exception:
        #     time.sleep(float(2000) / 2000)
        #     #wd.switch_to.alert.accept()

        wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        is_alert_present(self.browser, True)
        wd.find_element_by_id("PageControlPostingType_FromInn_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInn_I").send_keys("7736050003")
        wd.find_element_by_css_selector("#PageControlPostingType_FromKpp > tbody > tr > td.dxic").click()
        wd.find_element_by_id("PageControlPostingType_FromKpp_I").click()
        wd.find_element_by_id("PageControlPostingType_FromKpp_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromKpp_I").send_keys("997250001")
        wd.find_element_by_id("PageControlPostingType_FromInn_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInn_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInn_I").send_keys("773605000312")
        wd.find_element_by_id("PageControlPostingType_FromKpp_I").click()
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").click()
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").send_keys("Ивано Иван Иванович")
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").click()
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToFullName_I").send_keys("Иванов Иван Иванович")
        wd.find_element_by_id("PageControlPostingType_ToSettlement_I").click()
        wd.find_element_by_id("PageControlPostingType_ToSettlement_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToSettlement_I").send_keys("город")
        wd.find_element_by_id("PageControlPostingType_ToStreet_I").click()
        wd.find_element_by_id("PageControlPostingType_ToStreet_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToStreet_I").send_keys("улица")
        wd.find_element_by_id("PageControlPostingType_ToHome_I").click()
        wd.find_element_by_id("PageControlPostingType_ToHome_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToHome_I").send_keys("дом")
        wd.find_element_by_id("PageControlPostingType_ToFlat_I").click()
        wd.find_element_by_id("PageControlPostingType_ToFlat_I").clear()
        wd.find_element_by_id("PageControlPostingType_ToFlat_I").send_keys("4")
        wd.find_element_by_id("FillFormButton2").click()
        time.sleep(float(2000) / 2000)
        wd.find_element_by_id("PageControlPostingType_AttachName0_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachName0_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachName0_I").send_keys()
        wd.find_element_by_id("PageControlPostingType_AttachName0_I").click()
        wd.find_element_by_id("PageControlPostingType_AttachName0_I").clear()
        wd.find_element_by_id("PageControlPostingType_AttachName0_I").send_keys("Рубашка х/б")
        wd.find_element_by_id("PageControlPostingType_AttachCount0_I").click()
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
        wd.find_element_by_css_selector(
            "#PageControlPostingType_AttachCountry0_B-1 > table.dxbebt > tbody > tr > td.dx").click()
        time.sleep(float(2000) / 2000)
        wd.find_element_by_id("PageControlPostingType_AttachCountry0_DDD_L_LBI2T0").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterRequisites_I").send_keys("111111")
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterPhone_I").send_keys("111111")
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterFax_I").send_keys("111111")
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").click()
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromImporterEmail_I").send_keys("qqq@qq.ru")
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").click()
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromLicense_I").send_keys("12345")
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromLicense2_I").send_keys("12345")
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCertificate_I").send_keys("12345")
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCertificate2_I").send_keys("12345")
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber_I").send_keys("12345")
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").click()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromInvoiceNumber2_I").send_keys("12345")
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").click()
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromDeclaredValue_I").send_keys("1000")
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCashOnDeliverySum_I").send_keys("100")
        wd.find_element_by_id("PageControlPostingType_DdlCurrencyOnDelivery_B-1").click()
        time.sleep(float(2000) / 2000)
        wd.find_element_by_id("PageControlPostingType_DdlCurrencyOnDelivery_DDD_L_LBI115T0").click()
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromParcelsNumber_I").send_keys("12345")
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").click()
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").send_keys("12345")
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").click()
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").send_keys("примечание")
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").click()
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromNotes_I").send_keys("примечание")
        wd.find_element_by_id("PageControlPostingType_FromCurrentPostAccountNumber_I").click()
        wd.find_element_by_css_selector("#PageControlPostingType_FromNotes > tbody > tr > td.dxic").click()
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").click()
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").clear()
        wd.find_element_by_id("PageControlPostingType_FromDistribLackInstructionsPeriod_I").send_keys("30")
        wd.find_element_by_css_selector("#PageControlPostingType_ASPxButton2_CD > span").click()
        is_alert_present(self.browser, True)
        #wd.find_element_by_name("PageControlPostingType$ASPxButton2").click()
        is_alert_present(self.browser, False)
        self.assertTrue(success)

        # try:
        #     wd.find_element_by_css_selector("#PageControlPostingType_ASPxButton2_CD > span").click()
        #     wd.find_element_by_css_selector("#PageControlPostingType_ASPxButton2_CD > span").click()
        # except Exception:
        #     time.sleep(float(2000) / 2000)
        # try:
        #     wd.find_element_by_name("PageControlPostingType$ASPxButton2").click()
        # except Exception:
        #     time.sleep(float(2000) / 2000)
        # self.assertTrue(success)

    def tearDown(self):
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
