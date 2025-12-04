"""Singleton TypeDB connection instance"""

from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from typedb.api.connection.driver import Driver
from typedb.api.connection.transaction import Transaction, TransactionType
from typedb.driver import Credentials, DriverOptions, TypeDB

from app.core.config import settings


def connection() -> Driver:
    """TypeDB connection if not exists, create new database

    Returns
    -------
    Driver
        TypeDB Driver instance
    """
    credentials = Credentials(
        username=settings.typedb_username,
        password=settings.typedb_password,
    )
    driver = TypeDB.driver(
        address=settings.typedb_uri,
        credentials=credentials,
        driver_options=DriverOptions(),
    )

    if not driver.databases.contains(settings.typedb_database):
        driver.databases.create(settings.typedb_database)

    return driver


typedb_driver = connection()


@asynccontextmanager
async def get_transaction(
    transaction_type: TransactionType,
) -> AsyncGenerator[Transaction, Any]:
    """Get TypeDB transaction

    Parameters
    ----------
    transaction_type : TransactionType
        TypeDB transaction type

    Yields
    ------
    AsyncGenerator[Transaction, Any]
        TypeDB Transaction instance
    """

    tx = typedb_driver.transaction(
        database_name=settings.typedb_database,
        transaction_type=transaction_type,
    )

    try:
        yield tx
    finally:
        if tx.is_open():
            tx.close()
