# -*- coding: utf-8 -*-
from sqlalchemy import DateTime


def todict(self):
    """Method to turn an SA instance into a dict so we can output to json"""

    def convert_datetime(value):
        """We need to treat datetime's special to get them to json"""
        if value:
            return value.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return ""

    for col in self.__table__.columns:
        if isinstance(col.type, DateTime):
            value = convert_datetime(getattr(self, col.name))
        else:
            value = getattr(self, col.name)

        yield(col.name, value)


def iterfunc(self):
    """Returns an iterable that supports .next()
        so we can do dict(sa_instance)

    """
    return self.__todict__()


def fromdict(self, values):
    """Merge in items in the values dict into our object

       if it's one of our columns

    """
    for col in self.__table__.columns:
        if col.name in values:
            setattr(self, col.name, values[col.name])
