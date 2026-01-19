from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from infrastructure.database.repositories import OrganizationsRepository
from infrastructure.dependencies import Container, get_static_api_key
from interface_adapters.controllers import (
    GetByActivityIdController,
    GetByActivityNameController,
    GetByBuildingController,
    GetByNameController,
)
from interface_adapters.outgoing_dtos import (
    OutgoingOrganizationDTO,
    OutgoingOrganizationActivityNameDTO,
    OutgoingOrganizationByActivityDTO,
)


organizations_router = APIRouter(prefix='/organizations')

@organizations_router.get('/get-by-building')
@inject
async def get_by_building(
    building_id: int | None = None,
    database_uow = Depends(Provide[Container.unit_of_work]),
    _ = Depends(get_static_api_key),
) -> list[OutgoingOrganizationDTO]:
    async with database_uow:
        controller = GetByBuildingController(
            building_id=building_id, 
            repository=OrganizationsRepository(session=database_uow.session),
        )

        return await controller.execute()

@organizations_router.get('/get-by-activity-id')
@inject
async def get_by_activity_id(
    activity_id: int | None = None,
    database_uow = Depends(Provide[Container.unit_of_work]),
    _ = Depends(get_static_api_key),
) -> list[OutgoingOrganizationByActivityDTO]:
    async with database_uow:
        controller = GetByActivityIdController(
            activity_id=activity_id,
            repository=OrganizationsRepository(session=database_uow.session),
        )

        return await controller.execute()
    
@organizations_router.get('/get-by-activity-name')
@inject
async def get_by_activity_name(
    activity_name: str | None = None,
    database_uow = Depends(Provide(Container.unit_of_work)),
    _ = Depends(get_static_api_key),
) -> list[OutgoingOrganizationActivityNameDTO]:
    async with database_uow:
        controller = GetByActivityNameController(
            activity_name=activity_name,
            repository=OrganizationsRepository(session=database_uow.session),
        )

        return await controller.execute()
    
@organizations_router.get('/get-by-name')
@inject
async def get_by_activity_name(
    name: str | None = None,
    database_uow = Depends(Provide(Container.unit_of_work)),
    _ = Depends(get_static_api_key),
) -> list[OutgoingOrganizationDTO]:
    async with database_uow:
        controller = GetByNameController(
            name=name,
            repository=OrganizationsRepository(session=database_uow.session),
        )

        return await controller.execute()
