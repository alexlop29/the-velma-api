"""update id in locations table

Revision ID: bb5909e3b64f
Revises: db66f411b247
Create Date: 2023-05-13 18:05:50.000379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb5909e3b64f'
down_revision = 'db66f411b247'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        'locations',
        'id',
        new_column_name='location_id'
    )

def downgrade() -> None:
    op.alter_column(
        'locations',
        'location_id',
        new_column_name='id'
    )
