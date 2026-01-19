from fastapi import FastAPI

from infrastructure.handlers import buildings_router, organizations_router


def setup_handlers(application: FastAPI) -> None:
    '''
    Include application routers.
    '''
    application.include_router(buildings_router)
    application.include_router(organizations_router)
