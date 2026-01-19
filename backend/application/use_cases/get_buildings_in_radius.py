from application.ports import BuildingsRepositoryPort


class GetInRadiusUseCase:

    def __init__(self, latitude: float, longitude: float, radius: int, repository: BuildingsRepositoryPort) -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.repository = repository

    async def execute(self) -> list:
        return await self.repository.get_buildings_in_radius(
            latitude=self.latitude,
            longitude=self.longitude,
            radius=self.radius,
        )
