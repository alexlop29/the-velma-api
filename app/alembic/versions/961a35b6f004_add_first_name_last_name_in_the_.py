"""add first_name, last_name  in the characters table

Revision ID: 961a35b6f004
Revises: 37be4e1ffe24
Create Date: 2023-05-13 18:12:09.308046

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '961a35b6f004'
down_revision = '37be4e1ffe24'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'characters', 
        sa.Column('first_name', sa.VARCHAR, nullable=False)
    )
    op.add_column(
        'characters', 
        sa.Column('last_name', sa.VARCHAR, nullable=False)
    )

def downgrade() -> None:
    op.drop_column(
        'characters', 
        'first_name'
    )
    op.drop_column(
        'characters', 
        'last_name'
    )
