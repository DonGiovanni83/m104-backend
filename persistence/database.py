import os

import sqlalchemy.engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import Session

import persistence

db_host = os.environ["DB_HOST"]
db_port = os.environ["DB_PORT"]
db_name = os.environ["DB_NAME"]
db_user = os.environ["DB_USER"]
db_passwd = os.environ["DB_PASSWORD"]

engine: sqlalchemy.engine.Engine = None
session: Session = None


async def connect():
    global engine, session
    if engine is None or session is None:
        await create_db_engine_async()


async def close():
    global session
    session.close()


async def init_db():
    global engine
    if engine is None or session is None:
        await create_db_engine_async()

    async with engine.begin() as conn:
        await conn.run_sync(persistence.Base.metadata.create_all)


async def create_db_engine_async():
    global engine

    engine = create_async_engine(
        f"postgresql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}",
        echo=True
    )


async def get_session() -> AsyncSession:
    global session, engine
    if engine is None or session is None:
        await create_db_engine_async()
    session = AsyncSession(bind=engine)
    return session
