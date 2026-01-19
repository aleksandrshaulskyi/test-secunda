from application.ports import OrganizationsRepositoryPort


class GetOrganizationByActivityIdUseCase:

    def __init__(self, activity_id: int, repository: OrganizationsRepositoryPort) -> None:
        self.activity_id = activity_id
        self.repository = repository

    async def execute(self) -> list:
        return await self.repository.get_by_activity_id(activity_id=self.activity_id)
