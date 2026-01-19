from sqlalchemy import select, cast
from sqlalchemy.ext.asyncio import AsyncSession
from geoalchemy2.functions import ST_DWithin, ST_MakeEnvelope, ST_MakePoint, ST_Within
from geoalchemy2 import Geography

from application.ports import BuildingsRepositoryPort
from infrastructure.database.models.building import BuildingModel


class BuildingsRepository(BuildingsRepositoryPort):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_buildings_in_radius(
        self,
        latitude: float,
        longitude: float,
        radius: int
    ) -> list:
        statement = (
            select(
                BuildingModel.__table__.columns.id,
                BuildingModel.__table__.columns.address,
            ).where(
                ST_DWithin(
                    cast(BuildingModel.__table__.columns.location, Geography),
                    cast(
                        ST_MakePoint(longitude, latitude),
                        Geography,
                    ),
                    radius,
                )
            )
        )

        result = await self.session.execute(statement=statement)

        if (rows := result.mappings().all()):
            return rows
        return []
    
    async def get_buildings_in_rectangle(
        self,
        minimum_latitude: float,
        minimum_longitude: float,
        maximum_latitude: float,
        maximum_longitude: float,
    ) -> list:
        rectangle = ST_MakeEnvelope(
            minimum_longitude,
            minimum_latitude,
            maximum_longitude,
            maximum_latitude,
            4326,
        )

        statement = (
            select(
                BuildingModel.__table__.columns.id,
                BuildingModel.__table__.columns.address,
            )
            .where(
                ST_Within(
                    BuildingModel.__table__.columns.location,
                    rectangle,
                )
            )
        )

        result = await self.session.execute(statement)
        return result.mappings().all()
