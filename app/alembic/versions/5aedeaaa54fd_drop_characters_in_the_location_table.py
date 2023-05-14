"""drop characters in the location table

Revision ID: 5aedeaaa54fd
Revises: 961a35b6f004
Create Date: 2023-05-13 18:23:07.222053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5aedeaaa54fd'
down_revision = '961a35b6f004'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column(
        'locations', 
        'characters'
    )

def downgrade() -> None:
    op.add_column(
        'locations', 
        sa.Column('characters', sa.VARCHAR)
    )
