"""Add rental_price to cars

Revision ID: fc42664f6308
Revises: 98612c4c511b
Create Date: 2025-06-02 14:15:42.124349

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc42664f6308'
down_revision: Union[str, None] = '98612c4c511b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def downgrade():
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_make_model', ['make', 'model'])

def upgrade():
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.drop_constraint('uq_make_model', type_='unique')
