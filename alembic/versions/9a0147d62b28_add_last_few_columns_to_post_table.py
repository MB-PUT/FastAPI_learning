"""add last few  columns to post table

Revision ID: 9a0147d62b28
Revises: 71833cd300c5
Create Date: 2023-08-25 12:57:17.200763

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9a0147d62b28'
down_revision: Union[str, None] = '71833cd300c5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('published',sa.Boolean(),nullable=False,server_default='TRUE'))
    op.add_column('posts',sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts',column_name='published')
    op.drop_column('posts',column_name='created_at')
    pass
