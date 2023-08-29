"""add content column to post table

Revision ID: 9fd818ede5a3
Revises: 4ed09a63fa5d
Create Date: 2023-08-25 12:24:46.649747

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9fd818ede5a3'
down_revision: Union[str, None] = '4ed09a63fa5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
