"""drop last_seen_at in the characters table

Revision ID: 71919e77b58d
Revises: 893797fe83e0
Create Date: 2023-05-13 17:34:22.320554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71919e77b58d'
down_revision = '893797fe83e0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column(
        'characters', 
        'last_seen_at'
    )


def downgrade() -> None:
    op.add_column(
        'characters', 
        sa.Column('last_seen_at', sa.VARCHAR())
    )
