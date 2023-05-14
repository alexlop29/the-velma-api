"""drop name in the characters table

Revision ID: 37be4e1ffe24
Revises: 40e39b6c5a63
Create Date: 2023-05-13 18:10:56.550961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37be4e1ffe24'
down_revision = '40e39b6c5a63'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_column(
        'characters', 
        'name'
    )


def downgrade() -> None:
    op.add_column(
        'characters', 
        sa.Column('name', sa.VARCHAR)
    )
