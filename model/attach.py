# -*- coding: utf-8 -*-

class attach:
    def __init__(self, attach_name=None, count=None, weight=None, cost=None, TNVED=None, country=None):
        self.attach_name = attach_name
        self.count = count
        self.weight = weight
        self.cost = cost
        self.TNVED = TNVED
        self.country = country

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.attach_name, self.count, self.weight, self.cost, self.TNVED, self.country)

    def __eq__(self, other):
        return self.attach_name == other.country and \
               self.count == other.category and \
               self.weight == other.ph_or_ur and \
               self.cost == other.ph_or_ur and \
               self.TNVED == other.ph_or_ur and \
               self.country == other.ph_or_ur

attachs = []




