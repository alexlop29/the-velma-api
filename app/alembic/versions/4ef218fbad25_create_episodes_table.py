"""create episodes table

Revision ID: 4ef218fbad25
Revises: 7c1dd4ca2858
Create Date: 2023-05-13 13:32:00.848015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ef218fbad25'
down_revision = '7c1dd4ca2858'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'episodes',
        sa.Column('episode', sa.Integer, nullable=False, primary_key=True),
        sa.Column('name', sa.VARCHAR, nullable=False),
        sa.Column('air_date', sa.DATE, nullable=False),
        sa.Column('characters', sa.ARRAY(sa.VARCHAR), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('episodes')
