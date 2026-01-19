from application.ports import OrganizationsRepositoryPort
from application.use_cases import GetOrganizationByActivityNameUseCase
from interface_adapters.outgoing_dtos import OutgoingOrganizationActivityNameDTO


class GetByActivityNameController:

    def __init__(self, activity_name: str, repository: OrganizationsRepositoryPort) -> None:
        self.activity_name = activity_name
        self.repository = repository

    async def execute(self) -> list:
        use_case = GetOrganizationByActivityNameUseCase(activity_name=self.activity_name, repository=self.repository)

        organizations = await use_case.execute()

        return [OutgoingOrganizationActivityNameDTO(**organization) for organization in organizations]
