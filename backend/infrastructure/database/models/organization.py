from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import BaseModel


class OrganizationModel(BaseModel):
    __tablename__ = 'organization'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    building_id: Mapped[int] = mapped_column(
        ForeignKey('building.id'),
        nullable=False,
    )

    building: Mapped['BuildingModel'] = relationship(
        back_populates='organizations',
    )

    phones: Mapped[list['PhoneModel']] = relationship(
        back_populates='organization',
        cascade='all, delete-orphan',
    )

    organization_activities: Mapped[list['OrganizationActivityModel']] = relationship(
        back_populates='organization',
        cascade='all, delete-orphan',
    )

    activities: Mapped[list['ActivityModel']] = relationship(
        secondary='organization_activity',
        viewonly=True,
    )
