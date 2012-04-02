# -*- coding: utf-8 -*-
from zope.sqlalchemy import ZopeTransactionExtension
from easy_sqlalchemy import meta
from sqlalchemy import orm
from sqlalchemy import create_engine
import json
import random


def init_sqlalchemy(settings):
    # master
    master_url = settings['sqlalchemy.url']
    connect_kwargs = settings.get('sqlalchemy.connect_kwargs')
    kwargs = {}
    if connect_kwargs is not None:
        if isinstance(connect_kwargs, basestring):
            connect_kwargs = json.loads(connect_kwargs)
        for k, v in connect_kwargs.items():
            kwargs[k] = v
    engine = create_engine(master_url, **kwargs)
    sm = orm.sessionmaker(bind=engine, extension=ZopeTransactionExtension())
    meta.Session = orm.scoped_session(sm)
    meta.metadata.bind = engine

    # slaves
    slaves_url = settings.get('sqlalchemy.slaves', [])
    slaves = []
    for url in slaves_url:
        slave = create_engine(url, **kwargs)
        sm = orm.sessionmaker(bind=slave, extension=ZopeTransactionExtension())
        slaves.append(orm.scoped_session(sm))

    if slaves:
        slave = random.choice(slaves)
        meta.BaseObject.query = slave.query_property(orm.Query)
    else:
        meta.BaseObject.query = meta.Session.query_property(orm.Query)


def includeme(config):
    init_sqlalchemy(config.registry.settings)
