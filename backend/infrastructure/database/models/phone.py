from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.models.base import BaseModel


class PhoneModel(BaseModel):
    __tablename__ = 'phone'

    id: Mapped[int] = mapped_column(primary_key=True)

    number: Mapped[str] = mapped_column(
        String(32),
        nullable=False,
    )

    organization_id: Mapped[int] = mapped_column(
        ForeignKey('organization.id', ondelete='CASCADE'),
        nullable=False,
    )

    organization: Mapped['OrganizationModel'] = relationship(
        back_populates='phones',
    )

    __table_args__ = (
        UniqueConstraint('organization_id', 'number'),
    )
