from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import BaseModel


class OrganizationActivityModel(BaseModel):
    __tablename__ = 'organization_activity'

    organization_id: Mapped[int] = mapped_column(
        ForeignKey('organization.id', ondelete='CASCADE'),
        primary_key=True,
    )

    activity_id: Mapped[int] = mapped_column(
        ForeignKey('activity.id', ondelete='CASCADE'),
        primary_key=True,
    )

    organization: Mapped['OrganizationModel'] = relationship(
        back_populates='organization_activities',
    )

    activity: Mapped['ActivityModel'] = relationship(
        back_populates='organization_activities',
    )
