from fastapi import FastAPI

from lifespan import lifespan

from infrastructure.handlers import setup_handlers


def compose_application() -> FastAPI:
    '''
    Compose an instance of the FastAPI application.

    - Setup handlers.

    Returns:
        application: An instance of the FastAPI application.
    '''
    application = FastAPI(lifespan=lifespan)

    setup_handlers(application=application)

    return application
