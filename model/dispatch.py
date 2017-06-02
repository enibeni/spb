# -*- coding: utf-8 -*-

class dispatch:
    def __init__(self, country=None, category=None, ph_or_ur=None, blank_type=None):
        self.country = country
        self.category = category
        self.ph_or_ur = ph_or_ur
        self.blank_type = blank_type


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.country, self.category, self.ph_or_ur, self.blank_type)


    def __eq__(self, other):
        return self.country == other.country and \
               self.category == other.category and \
               self.ph_or_ur == other.ph_or_ur and \
               (self.blank_type is None or self.blank_type == other.blank)