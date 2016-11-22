class dispatch:
    def __init__(self, country=None, category=None, ph_or_ur=None, blank=None):
        self.country = country
        self.category = category
        self.ph_or_ur = ph_or_ur
        self.blank = blank


def __repr__(self):
    return "%s:%s:%s:%s" % (self.country, self.category, self.ph_or_ur, self.blank)


def __eq__(self, other):
    return self.conutry == other.country and \
           self.category == other.category and \
           self.ph_or_ur == other.ph_or_ur and \
           (self.blank is None or self.blank == other.blank)