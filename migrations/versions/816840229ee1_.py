"""empty message

Revision ID: 816840229ee1
Revises: 
Create Date: 2019-09-08 22:11:49.326339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '816840229ee1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=True),
    sa.Column('last_active', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session')
    op.drop_table('user')
    # ### end Alembic commands ###