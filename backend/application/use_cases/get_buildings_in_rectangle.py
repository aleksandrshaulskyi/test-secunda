from application.ports import BuildingsRepositoryPort


class GetInRectangleUseCase:

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
        return await self.repository.get_buildings_in_rectangle(
            minimum_latitude=self.minimum_latitude,
            minimum_longitude=self.minimum_longitude,
            maximum_latitude=self.maximum_latitude,
            maximum_longitude=self.maximum_longitude,
        )
