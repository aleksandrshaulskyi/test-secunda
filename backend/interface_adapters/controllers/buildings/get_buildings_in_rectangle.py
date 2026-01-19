from application.ports import BuildingsRepositoryPort
from application.use_cases import GetInRectangleUseCase
from interface_adapters.outgoing_dtos import OutgoingBuildingDTO


class GetBuildingsInRectangleController:

    def __init__(
        self,
        minimum_latitude: float,
        minimum_longitude: float,
        maximum_latitude: float,
        maximum_longitude: float,
        repository: BuildingsRepositoryPort,
    ) -> None:
        self.minimum_latitude = minimum_latitude
        self.minimum_longitude = minimum_longitude
        self.maximum_latitude = maximum_latitude
        self.maximum_longitude = maximum_longitude
        self.repository = repository

    async def execute(self) -> list:
        use_case = GetInRectangleUseCase(
            minimum_latitude=self.minimum_latitude,
            minimum_longitude=self.minimum_longitude,
            maximum_latitude=self.maximum_latitude,
            maximum_longitude=self.maximum_longitude,
            repository=self.repository,
        )

        buildings = await use_case.execute()

        return [OutgoingBuildingDTO(**building) for building in buildings]
