"""change id in the episodes table

Revision ID: 3c80cf16dd82
Revises: 5aedeaaa54fd
Create Date: 2023-05-13 18:26:03.844881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c80cf16dd82'
down_revision = '5aedeaaa54fd'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column(
        'episodes',
        'episode',
        new_column_name='episode_id'
    )

def downgrade() -> None:
    op.alter_column(
        'locations',
        'episode_id',
        new_column_name='episode'
    )
