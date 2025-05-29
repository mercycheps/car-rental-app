"""Your message

Revision ID: bb451654d9e1
Revises: b298c11da55e
Create Date: 2025-05-28 18:49:55.392685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa



revision: str = 'bb451654d9e1'
down_revision: Union[str, None] = 'b298c11da55e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Drop customers table
    # op.drop_table('customers')

    # Rename old rentals table
    op.rename_table('rentals', 'old_rentals')

    # Recreate rentals table with new schema
    op.create_table(
        'rentals',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('car_id', sa.Integer, sa.ForeignKey('cars.id'), nullable=False),
        sa.Column('start_date', sa.Date, nullable=True),
        sa.Column('end_date', sa.Date, nullable=False),
    )

    # Migrate data 
    op.execute("""
        INSERT INTO rentals (id, car_id, start_date)
        SELECT id, car_id, start_date FROM old_rentals
    """)

    # Drop the old rentals table
    op.drop_table('old_rentals')

