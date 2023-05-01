"""create characters table

Revision ID: 7c1dd4ca2858
Revises: 
Create Date: 2023-05-01 10:11:31.826464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c1dd4ca2858'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'characters',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.VARCHAR, nullable=False),
        sa.Column('species', sa.VARCHAR, nullable=False),
        sa.Column('gender', sa.VARCHAR, nullable=False),
        sa.Column('first_seen_at', sa.VARCHAR, nullable=False),
        sa.Column('last_seen_at', sa.VARCHAR, nullable=False),
        sa.Column('episodes', sa.ARRAY(sa.VARCHAR), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('characters')

