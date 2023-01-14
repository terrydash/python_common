# coding: utf-8
from sqlalchemy import Column, MetaData, Table, VARCHAR
from sqlalchemy.dialects.oracle.base import NUMBER

metadata = MetaData()


t_kcb = Table(
    'kcb', metadata,
    Column('xkkh', VARCHAR(40), index=True),
    Column('xqj', NUMBER(asdecimal=False)),
    Column('djj', NUMBER(asdecimal=False)),
    Column('skcd', NUMBER(asdecimal=False)),
    Column('dsz', VARCHAR(6)),
    Column('qsz', NUMBER(asdecimal=False)),
    Column('jsz', NUMBER(asdecimal=False)),
    Column('kcb', VARCHAR(800))
)
