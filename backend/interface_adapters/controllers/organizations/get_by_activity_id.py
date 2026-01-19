from application.ports import OrganizationsRepositoryPort
from application.use_cases import GetOrganizationByActivityIdUseCase
from interface_adapters.outgoing_dtos import OutgoingOrganizationByActivityDTO


class GetByActivityIdController:

    def __init__(self, activity_id: int, repository: OrganizationsRepositoryPort) -> None:
        self.activity_id = activity_id
        self.repository = repository

    async def execute(self) -> list:
        use_case = GetOrganizationByActivityIdUseCase(activity_id=self.activity_id, repository=self.repository)

        organizations = await use_case.execute()

        return [OutgoingOrganizationByActivityDTO(**organization) for organization in organizations]
