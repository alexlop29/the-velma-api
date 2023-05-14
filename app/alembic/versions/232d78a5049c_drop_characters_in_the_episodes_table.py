"""drop characters in the episodes table

Revision ID: 232d78a5049c
Revises: 3c80cf16dd82
Create Date: 2023-05-13 18:29:28.732973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '232d78a5049c'
down_revision = '3c80cf16dd82'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.drop_column(
        'episodes', 
        'characters'
    )


def downgrade() -> None:
    op.add_column(
        'episodes', 
        sa.Column('characters', sa.ARRAY(sa.VARCHAR), nullable=False),
    )
