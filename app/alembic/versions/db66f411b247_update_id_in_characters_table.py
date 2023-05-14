"""update id in characters table

Revision ID: db66f411b247
Revises: e93388e4d7a4
Create Date: 2023-05-13 18:04:13.677523

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db66f411b247'
down_revision = 'e93388e4d7a4'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        'characters',
        'id',
        new_column_name='character_id'
    )

def downgrade() -> None:
    op.alter_column(
        'characters',
        'character_id',
        new_column_name='id'
    )
