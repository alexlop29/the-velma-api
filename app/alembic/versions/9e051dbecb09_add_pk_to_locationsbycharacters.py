"""Add PK to LocationsByCharacters

Revision ID: 9e051dbecb09
Revises: db34c27a429d
Create Date: 2023-05-23 20:11:05.152647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e051dbecb09'
down_revision = 'db34c27a429d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'locations_visited_by_characters', sa.Column('id', sa.Integer, primary_key=True)
    )


def downgrade() -> None:
    op.drop_column(
        'locations_visited_by_characters', 
        'id'
    )
