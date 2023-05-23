"""Add PK to CharacterByEpisode

Revision ID: db34c27a429d
Revises: feefa1127573
Create Date: 2023-05-22 21:54:31.379697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db34c27a429d'
down_revision = 'feefa1127573'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        'character_appearances_by_episode', sa.Column('id', sa.Integer, primary_key=True)
    )


def downgrade() -> None:
    op.drop_column(
        'character_appearances_by_episode', 
        'id'
    )
