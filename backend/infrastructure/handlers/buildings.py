from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from infrastructure.database.repositories import BuildingsRepository
from infrastructure.dependencies import Container, get_static_api_key
from interface_adapters.controllers import GetBuildingsInRadiusController, GetBuildingsInRectangleController


buildings_router = APIRouter(prefix='/buildings')

@buildings_router.get('/get-in-radius')
@inject
async def get_in_radius(
    latitude: float,
    longitude: float,
    radius: int,
    database_uow = Depends(Provide[Container.unit_of_work]),
    _ = Depends(get_static_api_key),
) -> list:
    async with database_uow:
        controller = GetBuildingsInRadiusController(
            latitude=latitude,
            longitude=longitude,
            radius=radius,
            repository=BuildingsRepository(session=database_uow.session),
        )

        return await controller.execute()
    
@buildings_router.get('/get-in-rectangle')
@inject
async def get_in_rectangle(
    minimum_latitude: float,
    minimum_longitude: float,
    maximum_latitude: float,
    maximum_longitude: float,
    database_uow = Depends(Provide[Container.unit_of_work]),
    _ = Depends(get_static_api_key),
) -> list:
    async with database_uow:
        controller = GetBuildingsInRectangleController(
            minimum_latitude=minimum_latitude,
            minimum_longitude=minimum_longitude,
            maximum_latitude=maximum_latitude,
            maximum_longitude=maximum_longitude,
            repository=BuildingsRepository(session=database_uow.session),
        )

        return await controller.execute()
