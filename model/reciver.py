# -*- coding: utf-8 -*-

class reciver:
    def __init__(self, name=None, city=None, street=None, home=None):
        self.home = home
        self.street = street
        self.city = city
        self.name = name


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.name, self.city, self.street, self.home)


    def __eq__(self, other):
        return self.name == other.name and \
               self.city == other.city and \
               self.street == other.street and \
               self.home == other.home


