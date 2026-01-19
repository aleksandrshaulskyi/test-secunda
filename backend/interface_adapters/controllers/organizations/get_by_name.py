from application.ports import OrganizationsRepositoryPort
from application.use_cases import GetOrganizationsByNameUseCase
from interface_adapters.outgoing_dtos import OutgoingOrganizationDTO


class GetByNameController:

    def __init__(self, name: int, repository: OrganizationsRepositoryPort) -> None:
        self.name = name
        self.repository = repository

    async def execute(self) -> list:
        use_case = GetOrganizationsByNameUseCase(name=self.name, repository=self.repository)

        organizations = await use_case.execute()

        return [OutgoingOrganizationDTO(**organization) for organization in organizations]