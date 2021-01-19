import os

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
import sqlalchemy.engine
from sqlalchemy.orm import sessionmaker, Session

import persistence

engine: sqlalchemy.engine.Engine = None
session: Session = None
connection: sqlalchemy.engine.Connection = None


async def connect():
    global connection, engine, session
    if engine is None or session is None:
        await create_database_async()

    connection = engine.connect()


async def close():
    global connection
    session.close()
    connection.close()


async def create_database_async():
    global engine
    db_host = os.environ["DB_HOST"]
    db_port = os.environ["DB_PORT"]
    db_name = os.environ["DB_NAME"]
    db_user = os.environ["DB_USER"]
    db_passwd = os.environ["DB_PASSWORD"]

    engine = create_async_engine(
        f"postgresql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}",
        echo=True
    )
    async with engine.begin() as conn:
        await conn.run_sync(persistence.Base.metadata.create_all)


async def get_session() -> AsyncSession:
    global session, engine
    if engine is None or session is None:
        await create_database_async()
    session = AsyncSession(bind=engine)
    return session
