# -*- coding: utf-8 -*-

class sender:
    def __init__(self, company=None, fio=None, zipcode=None, region=None, city=None, street=None, home=None, inn=None, kpp=None):
        self.kpp = kpp
        self.inn = inn
        self.home = home
        self.street = street
        self.city = city
        self.region = region
        self.zipcode = zipcode
        self.fio = fio
        self.company = company



    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.company, self.fio,
                                self.zipcode, self.region,
                                self.city, self.street,
                                self.home, self.inn,
                                self.kpp)


    def __eq__(self, other):
        return (self.conutry is None or self.company == other.company) and \
               (self.fio is None or self.fio == other.fio) and \
               self.zipcode == other.zipcode and \
               self.region == other.region and \
               self.city == other.city and \
               self.street == other.street and \
               self.home == other.home and \
               self.inn == other.inn and \
               self.kpp == other.kpp

