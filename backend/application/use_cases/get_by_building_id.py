from application.ports import OrganizationsRepositoryPort


class GetOrganizationsByBuildingIdUseCase:

    def __init__(self, building_id: int, repository: OrganizationsRepositoryPort) -> None:
        self.building_id = building_id
        self.repository = repository

    async def execute(self) -> list:
        return await self.repository.get_by_building_id(building_id=self.building_id)
