from application.ports import OrganizationsRepositoryPort
from application.use_cases import GetOrganizationsByBuildingIdUseCase
from interface_adapters.outgoing_dtos import OutgoingOrganizationDTO


class GetByBuildingController:

    def __init__(self, building_id: int, repository: OrganizationsRepositoryPort) -> None:
        self.building_id = building_id
        self.repository = repository

    async def execute(self) -> list:
        use_case = GetOrganizationsByBuildingIdUseCase(building_id=self.building_id, repository=self.repository)

        organizations = await use_case.execute()

        return [OutgoingOrganizationDTO(**organization) for organization in organizations]
