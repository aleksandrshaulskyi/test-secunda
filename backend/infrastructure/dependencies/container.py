from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Singleton, Factory

from infrastructure.database import create_engine, create_session_factory, DatabaseUnitOfWork


class Container(DeclarativeContainer):
    database_engine = Singleton(create_engine)
    session_factory = Singleton(create_session_factory, engine=database_engine)

    unit_of_work = Factory(DatabaseUnitOfWork, session_factory=session_factory)
