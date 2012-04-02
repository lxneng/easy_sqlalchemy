# -*- coding: utf-8 -*-
from sqlalchemy import schema
from sqlalchemy.ext.declarative import declarative_base

Session = None

metadata = schema.MetaData()

BaseObject = declarative_base(metadata=metadata)

__all__ = ['Session', 'metadata', 'BaseObject']
