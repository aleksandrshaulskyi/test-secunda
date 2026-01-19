from sqlalchemy import String
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION
from sqlalchemy.orm import Mapped, mapped_column, relationship
from geoalchemy2 import Geometry

from infrastructure.database.models.base import BaseModel


class BuildingModel(BaseModel):
    __tablename__ = 'building'

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )

    address: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    location: Mapped[str] = mapped_column(
        Geometry(
            geometry_type='POINT',
            srid=4326,
            spatial_index=True,
        ),
        nullable=False,
    )

    organizations: Mapped[list['OrganizationModel']] = relationship(
        back_populates='building',
    )
