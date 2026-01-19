"""initial schema with postgis

Revision ID: 049ce7da6415
Revises:
Create Date: 2026-01-17 22:10:49.880409
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


revision: str = '049ce7da6415'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('CREATE EXTENSION IF NOT EXISTS postgis')

    op.create_table(
        'building',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('address', sa.String(length=255), nullable=False),
        sa.Column(
            'location',
            Geometry(
                geometry_type='POINT',
                srid=4326,
            ),
            nullable=False,
        ),
    )

    op.create_index(
        'ix_building_location',
        'building',
        ['location'],
        postgresql_using='gist',
    )

    op.create_table(
        'activity',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column(
            'parent_id',
            sa.Integer,
            sa.ForeignKey('activity.id', ondelete='CASCADE'),
            nullable=True,
        ),
        sa.UniqueConstraint(
            'parent_id',
            'name',
            name='uq_activity_parent_name',
        ),
    )

    op.create_table(
        'organization',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column(
            'building_id',
            sa.Integer,
            sa.ForeignKey('building.id', ondelete='RESTRICT'),
            nullable=False,
        ),
    )

    op.create_table(
        'phone',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('number', sa.String(length=32), nullable=False),
        sa.Column(
            'organization_id',
            sa.Integer,
            sa.ForeignKey('organization.id', ondelete='CASCADE'),
            nullable=False,
        ),
        sa.UniqueConstraint(
            'organization_id',
            'number',
            name='uq_phone_org_number',
        ),
    )

    op.create_table(
        'organization_activity',
        sa.Column(
            'organization_id',
            sa.Integer,
            sa.ForeignKey('organization.id', ondelete='CASCADE'),
            primary_key=True,
        ),
        sa.Column(
            'activity_id',
            sa.Integer,
            sa.ForeignKey('activity.id', ondelete='CASCADE'),
            primary_key=True,
        ),
    )


def downgrade() -> None:
    op.drop_table('organization_activity')
    op.drop_table('phone')
    op.drop_table('organization')
    op.drop_table('activity')

    op.drop_index('ix_building_location', table_name='building')
    op.drop_table('building')
