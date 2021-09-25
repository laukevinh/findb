from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Date
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy.sql.functions import current_timestamp
from .settings import CONNECTION

metadata_obj = MetaData()
house = Table('house_transactions', metadata_obj,
              Column('transaction_id', Integer, primary_key=True),
              Column('prefix', String(60)),
              Column('last', String(60), nullable=False),
              Column('first', String(60), nullable=False),
              Column('suffix', String(60)),
              Column('filing_type', String(60), key='filingtype'),
              Column('state_district', String(60), key='statedst'),
              Column('year', String(60)),
              Column('filing_date', Date(), key='filingdate'),
              Column('doc_id', String(60), key='docid'),
              Column('created_on', DateTime(),
                     server_default=current_timestamp()),
              Column('modified_on', DateTime(), onupdate=current_timestamp()),
              )


def create_tables():
    engine = create_engine(CONNECTION, future=True)
    house.create(engine, checkfirst=True)


def destroy_tables():
    engine = create_engine(CONNECTION, future=True)
    house.drop(engine)
