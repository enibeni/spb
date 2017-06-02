# -*- coding: utf-8 -*-

class blank:
    def __init__(self, requisities=None, phone=None, fax=None, email=None, licence=None,
                 licence2=None, cert=None, cert2=None, invoice=None, invoice2=None, declaired_value=None,
                 cash_on_delivery=None, currancy=None, parse_number=None, cur_post_number=None, note=None, period=None):
        self.requisities = requisities
        self.phone = phone
        self.fax = fax
        self.email = email
        self.licence = licence
        self.licence2 = licence2
        self.cert = cert
        self.cert2 = cert2
        self.invoice = invoice
        self.invoice2 = invoice2
        self.declaired_value = declaired_value
        self.cash_on_delivery = cash_on_delivery
        self.currancy = currancy
        self.parse_number = parse_number
        self.cur_post_number = cur_post_number
        self.note = note
        self.period = period


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.requisities,
                                self.phone, self.fax,
                                self.email, self.licence,
                                self.licence2, self.cert,
                                self.cert2, self.invoice,
                                self.invoice2, self.declaired_value,
                                self.cash_on_delivery, self.currancy,
                                self.parse_number, self.cur_post_number,
                                self.note, self.period)


    def __eq__(self, other):
        return self.requisities == other.imp_requisities and \
               self.phone == other.phone and \
               self.fax == other.imp_fax and \
               self.email == other.imp_email and \
               self.licence == other.imp_licence and \
               self.licence2 == other.imp_lecence2 and \
               self.cert == other.imp_cert and \
               self.cert2 == other.imp_cert2 and \
               self.invoice == other.imp_invoice and \
               self.invoice2 == other.imp_invoice2 and \
               self.declaired_value == other.imp_declaired_value and \
               self.cash_on_delivery == other.cash_on_delivery and \
               self.currancy == other.currancy and \
               self.parse_number == other.parse_nuber and \
               self.cur_post_number == other.cur_post_number and \
               self.note == other.note and \
               self.period == other.period

