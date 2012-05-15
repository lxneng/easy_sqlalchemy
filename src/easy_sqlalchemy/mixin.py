# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm.interfaces import MapperExtension


class BaseExtension(MapperExtension):
    def before_update(self, mapper, connection, instance):  
        """update updated_at time"""
        if instance.__table__.c.has_key('updated_at'):
            instance.updated_at = datetime.now()


class BaseMixin(object):
    __mapper_args__ = {'extension': BaseExtension()} 
