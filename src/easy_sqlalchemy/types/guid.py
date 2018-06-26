# -*- coding: utf-8 -*-
import uuid
from sqlalchemy.types import TypeDecorator
from sqlalchemy.types import CHAR
from sqlalchemy.dialects import postgresql


class GUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses CHAR(36), storing as
    stringified hex values.

    This implementation is based on the SQLAlchemy
    `backend-agnostic GUID Type
    <http://www.sqlalchemy.org/docs/core/types.html#backend-agnostic-guid-type>`_
    example.
    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(postgresql.UUID())
        else:
            return dialect.type_descriptor(CHAR(36))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return str(uuid.UUID(value))
            else:
                # hexstring
                return str(value)

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)
