"""Added initial shifts table

Revision ID: 47117b802b19
Revises: f1890659822f
Create Date: 2020-01-05 02:49:12.693028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47117b802b19'
down_revision = 'f1890659822f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('shift',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('department', sa.Integer(), nullable=False),
        sa.Column('start_time', sa.DateTime(), nullable=False),
        sa.Column('end_time', sa.Datetime(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )


def downgrade():
    pass
