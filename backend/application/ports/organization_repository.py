from abc import ABC, abstractmethod


class OrganizationsRepositoryPort(ABC):

    @abstractmethod
    async def get_by_building_id(self, building_id: int) -> list:
        ...

    @abstractmethod
    async def get_by_activity_id(self, activity_id: int) -> list:
        ...

    @abstractmethod
    async def get_by_activity_name(self, root_activity_name: str) -> list:
        ...

    @abstractmethod
    async def get_by_name(self, name: str) -> list:
        ...
