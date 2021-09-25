from sqlalchemy import delete
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine
from sqlalchemy import Table
from sqlalchemy import select


def get_data_by_year(engine: Engine, table: Table, year: str):
    with engine.begin() as connection:
        connection.execute(table.select())
        stmt = select(table).where(table.c.year == year)
        results = connection.execute(stmt)
        return results.all()


def insert_transactions(engine: Engine, table: Table, transactions):
    with engine.begin() as connection:
        connection.execute(table.select())
        stmt = insert(table)
        connection.execute(stmt, transactions)


def delete_rows_by_year(engine: Engine, table: Table, year: str):
    with engine.begin() as connection:
        connection.execute(table.select())
        stmt = delete(table).where(table.c.year == year)
        connection.execute(stmt)
