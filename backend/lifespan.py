from contextlib import asynccontextmanager

from fastapi import FastAPI

from infrastructure.dependencies import Container


@asynccontextmanager
async def lifespan(application: FastAPI):
    container = Container()

    container.wire(
        modules=[
            'infrastructure.handlers.organizations',
            'infrastructure.handlers.buildings',
        ]
    )

    yield
