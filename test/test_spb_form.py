import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_spb_form(app):
    app.open_home_page()
    app.dispatch.fill_dest_country()
    app.dispatch.fill_posting_type()
    app.go_to_second_form()
    # FORM 2
    app.sender.fill_company_name()
    app.sender.fill_zipcode()
    app.sender.fill_region()
    app.sender.fill_city()
    app.sender.fill_street()
    app.sender.fill_home()
    app.sender.fill_inn()
    app.sender.fill_kpp()
    app.reciver.fill_resiv_name()
    app.reciver.fill_resiv_city()
    app.reciver.fill_resiv_street()
    app.reciver.fill_resiv_home()
    app.go_to_third_form()
    # FORM 3
    app.blank.fill_dispatch()
    app.blank.fill_imp_requisities()
    app.blank.fill_imp_phone()
    app.blank.fill_imp_fax()
    app.blank.fill_imp_email()
    app.blank.fill_imp_license()
    app.blank.fill_imp_licence2()
    app.blank.fill_imp_cert()
    app.blank.fill_imp_cert2()
    app.blank.fill_imp_invoice()
    app.blank.fill_imp_invoice2()
    app.blank.fill_declaired_value()
    app.blank.fill_cash_on_delivery()
    app.blank.fill_currancy()
    app.blank.fill_parse_number()
    app.blank.fill_cur_post_number()
    app.blank.fill_note()
    app.blank.fill_period()
    app.form_blank()
