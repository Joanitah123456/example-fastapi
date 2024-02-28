"""add content column to posts table

Revision ID: ac50645cb29e
Revises: 3c5eac0b543b
Create Date: 2024-02-27 19:58:21.601378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ac50645cb29e'
down_revision: Union[str, None] = '3c5eac0b543b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass