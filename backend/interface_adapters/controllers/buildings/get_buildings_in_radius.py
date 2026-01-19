from application.ports import BuildingsRepositoryPort
from application.use_cases import GetInRadiusUseCase
from interface_adapters.outgoing_dtos import OutgoingBuildingDTO


class GetBuildingsInRadiusController:

    def __init__(self, latitude: float, longitude: float, radius: int, repository: BuildingsRepositoryPort) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.repository = repository

    async def execute(self) -> list:
        use_case = GetInRadiusUseCase(
            latitude=self.latitude,
            longitude=self.longitude,
            radius=self.radius,
            repository=self.repository,
        )

        buildings = await use_case.execute()

        return [OutgoingBuildingDTO(**building) for building in buildings]
