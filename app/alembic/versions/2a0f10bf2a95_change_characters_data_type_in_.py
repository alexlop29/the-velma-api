"""change characters data type in locations table

Revision ID: 2a0f10bf2a95
Revises: 6efadef0afd8
Create Date: 2023-05-13 15:09:50.297557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a0f10bf2a95'
down_revision = '6efadef0afd8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        'locations',
        'characters',
        type=sa.ARRAY(sa.VARCHAR()),
        existing_type=sa.VARCHAR()
    )

def downgrade() -> None:
    op.alter_column(
        'locations',
        'characters',
        type=sa.VARCHAR(),
        existing_type=sa.ARRAY(sa.VARCHAR())
    )
