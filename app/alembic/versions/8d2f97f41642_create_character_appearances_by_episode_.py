"""create character_appearances_by_episode table

Revision ID: 8d2f97f41642
Revises: 232d78a5049c
Create Date: 2023-05-13 18:32:19.652407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d2f97f41642'
down_revision = '232d78a5049c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'character_appearances_by_episode',
        sa.Column('character_id', sa.Integer, sa.ForeignKey('characters.character_id')),
        sa.Column('episode_id', sa.Integer, sa.ForeignKey('episodes.episode_id'))
    )

def downgrade() -> None:
    op.drop_table('character_appearances_by_episode')
