"""drop episodes in the characters table

Revision ID: e93388e4d7a4
Revises: 71919e77b58d
Create Date: 2023-05-13 17:34:56.842161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e93388e4d7a4'
down_revision = '71919e77b58d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column(
        'characters', 
        'episodes'
    )


def downgrade() -> None:
    op.add_column(
        'characters', 
        sa.Column('episodes', sa.ARRAY(sa.VARCHAR))
    )
