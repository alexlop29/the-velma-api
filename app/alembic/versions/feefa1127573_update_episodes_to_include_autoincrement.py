"""Update Episodes to include autoincrement

Revision ID: feefa1127573
Revises: 8d2f97f41642
Create Date: 2023-05-22 20:40:26.488579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'feefa1127573'
down_revision = '8d2f97f41642'
branch_labels = None
depends_on = None


def upgrade() -> None:
     op.alter_column(
        'episodes',
        'episode_id',
        existing_type=sa.Integer,
        autoincrement=True,
        nullable=False,
        primary_key=True
    )


def downgrade() -> None:
         op.alter_column(
        'episodes',
        'episode_id',
        existing_type=sa.Integer,
        autoincrement=False,
        nullable=False,
        primary_key=True
    )
