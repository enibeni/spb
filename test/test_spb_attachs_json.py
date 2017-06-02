# -*- coding: utf-8 -*-
from model.dispatch import dispatch
from model.sender import sender
from model.reciver import reciver
from model.attach import attach
from model.blank import blank


def test_spb_form(app, json_dispatch, json_sender, json_reciver, json_attachs, json_blank):
    dispatch = json_dispatch
    sender = json_sender
    reciver = json_reciver
    print("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + str(type(reciver)))
    attachs = json_attachs
    print("2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" + str(type(attachs)))
    print(attachs)
    blank = json_blank
    app.open_home_page()
    app.dispatch.fill_dest_country(dispatch.country)
    app.dispatch.fill_posting_type(dispatch.blank_type)
    app.go_to_second_form()
    # FORM 2
    app.sender.fill_company_name(sender.company)
    app.sender.fill_zipcode(sender.zipcode)
    app.sender.fill_region()
    app.sender.fill_city()
    app.sender.fill_street(sender.street)
    app.sender.fill_home(sender.home)
    app.sender.fill_inn(sender.inn)
    app.sender.fill_kpp(sender.kpp)
    app.reciver.fill_resiv_name(reciver.name)
    app.reciver.fill_resiv_city(reciver.city)
    app.reciver.fill_resiv_street(reciver.street)
    app.reciver.fill_resiv_home(reciver.home)
    app.go_to_third_form()
    # FORM 3
    app.attach.fill_attachs(attachs)
    app.blank.fill_requisities(blank.requisities)
    app.blank.fill_phone(blank.phone)
    app.blank.fill_fax(blank.fax)
    app.blank.fill_email(blank.email)
    app.blank.fill_licence(blank.licence)
    app.blank.fill_licence2(blank.licence2)
    app.blank.fill_cert(blank.cert)
    app.blank.fill_cert2(blank.cert2)
    app.blank.fill_invoice(blank.invoice)
    app.blank.fill_invoice2(blank.invoice2)
    app.blank.fill_declaired_value(blank.declaired_value)
    app.blank.fill_cash_on_delivery(blank.cash_on_delivery)
    # app.blank.fill_currancy("RUB, Российский рубль")
    app.blank.fill_parse_number(blank.parse_number)
    app.blank.fill_cur_post_number(blank.cur_post_number)
    app.blank.fill_note(blank.note)
    app.blank.fill_period(blank.period)
    app.form_blank()

    
