from application.ports import OrganizationsRepositoryPort


class GetOrganizationsByNameUseCase:

    def __init__(self, name: int, repository: OrganizationsRepositoryPort) -> None:
        self.name = name
        self.repository = repository

    async def execute(self) -> list:
        return await self.repository.get_by_name(name=self.name)
