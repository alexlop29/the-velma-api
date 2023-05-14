"""create locations_visited_by_character table

Revision ID: 40e39b6c5a63
Revises: bb5909e3b64f
Create Date: 2023-05-13 18:07:00.181110

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e39b6c5a63'
down_revision = 'bb5909e3b64f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'locations_visited_by_characters',
        sa.Column('character_id', sa.Integer, sa.ForeignKey('characters.character_id')),
        sa.Column('location_id', sa.Integer, sa.ForeignKey('locations.location_id'))
    )

def downgrade() -> None:
    op.drop_table('locations_visited_by_characters')
