# -*- coding: utf-8 -*-
from sqlalchemy import schema
from sqlalchemy.ext.declarative import declarative_base
from easy_sqlalchemy.ext import (
        todict,
        iterfunc,
        fromdict
        )


Session = None

metadata = schema.MetaData()

BaseObject = declarative_base(metadata=metadata)
BaseObject.__todict__ = todict
BaseObject.__iter__ = iterfunc
BaseObject.fromdict = fromdict


__all__ = ['Session', 'metadata', 'BaseObject']
