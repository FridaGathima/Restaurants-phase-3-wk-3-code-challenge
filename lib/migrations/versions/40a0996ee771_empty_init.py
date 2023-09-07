"""Empty Init

Revision ID: 40a0996ee771
Revises: bb4aa59e40a0
Create Date: 2023-09-04 12:54:31.538167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '40a0996ee771'
down_revision: Union[str, None] = 'bb4aa59e40a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
