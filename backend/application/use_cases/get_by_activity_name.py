from application.ports import OrganizationsRepositoryPort


class GetOrganizationByActivityNameUseCase:

    def __init__(self, activity_name: str, repository: OrganizationsRepositoryPort) -> None:
        self.activity_name = activity_name
        self.repository = repository

    async def execute(self) -> list:
        return await self.repository.get_by_activity_name(root_activity_name=self.activity_name)
