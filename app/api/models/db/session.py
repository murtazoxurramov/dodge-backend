from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.config import Config, load_config
from service.repo.repo import SQLAlchemyRepos


app_config: Config = load_config('app.ini')
DATABASE_URL = f"postgresql+asyncpg://{app_config.db.user}:{app_config.db.password}@{app_config.db.host}:{app_config.db.port}/{app_config.db.database}?async_fallback=True"
engine = create_async_engine(DATABASE_URL,
                             future=True,
                             echo=False,
                             pool_size=100,
                             max_overflow=0)


async def get_repo():
    async_session = sessionmaker(engine,
                                 expire_on_commit=False,
                                 class_=AsyncSession)
    try:
        async with async_session() as session:
            repo = SQLAlchemyRepos(session)
            yield repo
    finally:
        await session.close()
