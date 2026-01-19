from abc import ABC, abstractmethod


class BuildingsRepositoryPort(ABC):

    @abstractmethod
    async def get_buildings_in_radius(self, latitude: float, longitude: float, radius: int) -> list:
        ...

    @abstractmethod
    async def get_buildings_in_rectangle(
        self,
        minimum_longitude,
        minimum_latitude,
        maximum_longitude,
        maximum_latitude,
    ) -> list:
        ...
