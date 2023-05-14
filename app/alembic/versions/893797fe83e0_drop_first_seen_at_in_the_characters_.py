"""drop first_seen_at in the characters table

Revision ID: 893797fe83e0
Revises: 2a0f10bf2a95
Create Date: 2023-05-13 17:31:12.598424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '893797fe83e0'
down_revision = '2a0f10bf2a95'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column(
        'characters', 
        'first_seen_at'
    )


def downgrade() -> None:
    op.add_column(
        'characters', 
        sa.Column('first_seen_at', sa.VARCHAR())
    )
