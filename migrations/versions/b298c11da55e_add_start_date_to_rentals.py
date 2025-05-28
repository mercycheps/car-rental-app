"""Add start_date to rentals

Revision ID: b298c11da55e
Revises: 26458b0d0e00
Create Date: 2025-05-28 13:43:06.832075
"""

from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy.engine import reflection


# revision identifiers, used by Alembic.
revision: str = 'b298c11da55e'
down_revision: Union[str, None] = '26458b0d0e00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    bind = op.get_bind()
    dialect = bind.dialect.name

    # Add the start_date column
    op.add_column('rentals', sa.Column('start_date', sa.Date(), nullable=False))

    # SQLite does not support ALTER COLUMN to set NOT NULL
    if dialect != 'sqlite':
        op.alter_column('rentals', 'duration_days',
                        existing_type=sa.INTEGER(),
                        nullable=False)


def downgrade() -> None:
    bind = op.get_bind()
    dialect = bind.dialect.name

    # Only alter column if not using SQLite
    if dialect != 'sqlite':
        op.alter_column('rentals', 'duration_days',
                        existing_type=sa.INTEGER(),
                        nullable=True)

    # op.drop_column('rentals', 'start_date')
