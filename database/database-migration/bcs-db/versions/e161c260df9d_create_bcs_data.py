"""create bcs data

Revision ID: e161c260df9d
Revises: 
Create Date: 2022-07-29 16:46:15.260426

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column,String
from sqlalchemy.schema import Sequence, CreateSequence

# revision identifiers, used by Alembic.
revision = 'e161c260df9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
