from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import BaseModel


class ActivityModel(BaseModel):
    __tablename__ = 'activity'

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    parent_id: Mapped[int | None] = mapped_column(
        ForeignKey('activity.id', ondelete='CASCADE'),
        nullable=True,
    )

    parent: Mapped['ActivityModel | None'] = relationship(
        remote_side='ActivityModel.id',
        back_populates='children',
    )

    children: Mapped[list['ActivityModel']] = relationship(
        back_populates='parent',
        cascade='all, delete-orphan',
    )

    organization_activities: Mapped[list['OrganizationActivityModel']] = relationship(
        back_populates='activity',
        cascade='all, delete-orphan',
    )

    organizations: Mapped[list['OrganizationModel']] = relationship(
        secondary='organization_activity',
        back_populates='activities',
    )

    __table_args__ = (
        UniqueConstraint('parent_id', 'name'),
    )
