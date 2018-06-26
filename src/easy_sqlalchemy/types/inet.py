# -*- coding: utf-8 -*-
import IPy
from sqlalchemy.types import TypeDecorator
from sqlalchemy.types import CHAR
from sqlalchemy.dialects import postgresql


class INET(TypeDecorator):
    """Platform-independent INET type.

    This type stores IPv4 and IPv6 addresses and netmarks. This type
    uses the `IPy.IP <http://pypi.python.org/pypi/IPy>`_ instances
    to store values. As input it will accept also a standard python
    string.

    When using a PostgreSQL backend the native INET type is used. On
    other databases values are stored as CHAR(42).
    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(postgresql.INET())
        else:
            return dialect.type_descriptor(CHAR(42))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, IPy.IP):
                value = IPy.IP(value)
            return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return IPy.IP(value)
