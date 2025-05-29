"""Add unique constraint to Car (make, model)

Revision ID: 248975e6e8fb
Revises: 23fb034e7b70
Create Date: 2025-05-29 09:36:47.216826

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '248975e6e8fb'
down_revision: Union[str, None] = '23fb034e7b70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_make_model', ['make', 'model'])

def downgrade():
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.drop_constraint('uq_make_model', type_='unique')
