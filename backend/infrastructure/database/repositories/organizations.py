from sqlalchemy import func, select
from sqlalchemy.orm import aliased
from sqlalchemy.ext.asyncio import AsyncSession

from application.ports import OrganizationsRepositoryPort
from infrastructure.database.models import ActivityModel, BuildingModel, OrganizationModel, OrganizationActivityModel


class OrganizationsRepository(OrganizationsRepositoryPort):

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_by_building_id(self, building_id: int) -> list:
        statement = select(
            OrganizationModel.__table__,
        ).join(
            BuildingModel.__table__,
            BuildingModel.__table__.columns.id == OrganizationModel.__table__.columns.building_id,
        ).where(
            BuildingModel.__table__.columns.id == building_id,
        )

        result = await self.session.execute(statement=statement)

        if (rows := result.mappings().all()):
            return rows
        return []
    
    async def get_by_activity_id(self, activity_id: int) -> list:
        statement = (
            select(
                OrganizationModel.__table__.columns.id.label('organization_id'),
                OrganizationModel.__table__.columns.name.label('organization_name'),
                OrganizationModel.__table__.columns.building_id.label('building_id'),
                ActivityModel.__table__.columns.id.label('activity_id'),
                ActivityModel.__table__.columns.name.label('activity_name'),
            )
            .join(
                OrganizationActivityModel.__table__,
                OrganizationActivityModel.__table__.columns.organization_id
                == OrganizationModel.__table__.columns.id,
            )
            .join(
                ActivityModel.__table__,
                ActivityModel.__table__.columns.id
                == OrganizationActivityModel.__table__.columns.activity_id,
            )
            .where(
                OrganizationActivityModel.__table__.columns.activity_id == activity_id,
            )
        )

        result = await self.session.execute(statement=statement)

        if (rows := result.mappings().all()):
            return rows
        return []
    
    async def get_by_activity_name(self, root_activity_name: str) -> list:
        activity_tree_cte = (
            select(
                ActivityModel.__table__.columns.id,
            )
            .where(
                ActivityModel.__table__.columns.name == root_activity_name,
            )
            .cte(
                name='activity_tree',
                recursive=True,
            )
        )

        child_activity_table = aliased(ActivityModel.__table__)

        activity_tree_cte = activity_tree_cte.union_all(
            select(
                child_activity_table.columns.id,
            )
            .where(
                child_activity_table.columns.parent_id
                == activity_tree_cte.columns.id,
            )
        )

        statement = (
            select(
                OrganizationModel.__table__.columns.id
                    .label('organization_id'),

                OrganizationModel.__table__.columns.name
                    .label('organization_name'),

                OrganizationModel.__table__.columns.building_id
                    .label('building_id'),

                func.array_agg(
                    ActivityModel.__table__.columns.id
                ).label('activity_ids'),

                func.array_agg(
                    ActivityModel.__table__.columns.name
                ).label('activity_names'),
            )
            .join(
                OrganizationActivityModel.__table__,
                OrganizationActivityModel.__table__.columns.organization_id
                == OrganizationModel.__table__.columns.id,
            )
            .join(
                ActivityModel.__table__,
                ActivityModel.__table__.columns.id
                == OrganizationActivityModel.__table__.columns.activity_id,
            )
            .join(
                activity_tree_cte,
                activity_tree_cte.columns.id
                == ActivityModel.__table__.columns.id,
            )
            .group_by(
                OrganizationModel.__table__.columns.id,
                OrganizationModel.__table__.columns.name,
                OrganizationModel.__table__.columns.building_id,
            )
        )

        result = await self.session.execute(statement=statement)

        if (rows := result.mappings().all()):
            return rows
        return []
    
    async def get_by_name(self, name: str) -> list:
        statement = select(
            OrganizationModel.__table__,
        ).where(
            OrganizationModel.__table__.columns.name == name,
        )

        result = await self.session.execute(statement=statement)

        if (rows := result.mappings().all()):
            return rows
        return []
