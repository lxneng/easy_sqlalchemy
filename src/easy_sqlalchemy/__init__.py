# -*- coding: utf-8 -*-
from zope.sqlalchemy import register
from easy_sqlalchemy import meta
from sqlalchemy import orm
from sqlalchemy import create_engine
from sqlalchemy import event
from datetime import datetime
import json
import random


def updated_at_listener(mapper, connection, instance):
    if 'updated_at' in instance.__table__.c:
        instance.updated_at = datetime.now()


def init_sqlalchemy(settings):
    # master
    master_url = settings['sqlalchemy.url']
    connect_kwargs = settings.get('sqlalchemy.connect_kwargs')
    kwargs = {}
    if connect_kwargs is not None:
        if isinstance(connect_kwargs, str):
            connect_kwargs = json.loads(connect_kwargs)
        for k, v in connect_kwargs.items():
            kwargs[k] = v
    engine = create_engine(master_url, **kwargs)

    sm = orm.sessionmaker(bind=engine)
    ss = orm.scoped_session(sm)
    register(ss)
    meta.Session = ss
    meta.metadata.bind = engine

    # slaves
    slaves_url = settings.get('sqlalchemy.slaves', [])
    slaves = []
    for url in slaves_url:
        slave = create_engine(url, **kwargs)
        sm = orm.sessionmaker(bind=slave)
        ss = orm.scoped_session(sm)
        register(ss)
        slaves.append(ss)

    if slaves:
        slave = random.choice(slaves)
        meta.BaseObject.query = slave.query_property(orm.Query)
    else:
        meta.BaseObject.query = meta.Session.query_property(orm.Query)


def includeme(config):
    init_sqlalchemy(config.registry.settings)
    event.listen(orm.mapper, 'before_update', updated_at_listener)
