"""create locations table

Revision ID: 6efadef0afd8
Revises: 4ef218fbad25
Create Date: 2023-05-13 13:37:49.413079

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6efadef0afd8'
down_revision = '4ef218fbad25'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'locations',
        sa.Column('id', sa.Integer, nullable=False, primary_key=True),
        sa.Column('name', sa.VARCHAR, nullable=False),
        sa.Column('characters', sa.VARCHAR, nullable=False)
    )

def downgrade() -> None:
    op.drop_table('locations')
