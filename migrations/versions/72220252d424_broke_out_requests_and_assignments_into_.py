"""Broke out requests and assignments into separate tables

Revision ID: 72220252d424
Revises: ba06f3351d89
Create Date: 2019-11-21 01:57:11.194961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '72220252d424'
down_revision = 'ba06f3351d89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('badge_to_room_night', 'room_night_request')
    with op.batch_alter_table('room_night_request', schema=None) as batch_op:
        batch_op.drop_column('hotel_room')

    op.create_table('room_night_assignment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('badge', sa.Integer(), nullable=True),
    sa.Column('room_night', sa.Integer(), nullable=False),
    sa.Column('hotel_room', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['badge'], ['badge.id'], ),
    sa.ForeignKeyConstraint(['hotel_room'], ['hotel_room.id'], ),
    sa.ForeignKeyConstraint(['room_night'], ['hotel_room_night.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    with op.batch_alter_table('room_night_approval', schema=None) as batch_op:
        batch_op.drop_constraint('room_night_approval_room_night_fkey', type_='foreignkey')
        batch_op.create_foreign_key('room_night_approval_room_night_request_fkey', 'room_night_request', ['room_night'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('room_night_request', 'badge_to_room_night')
    with op.batch_alter_table('badge_to_room_night', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hotel_room', sa.Integer(), nullable=True))
        batch_op.add_constraint(sa.ForeignKeyConstraint(['hotel_room'], ['hotel_room.id'], ))

    with op.batch_alter_table('room_night_approval', schema=None) as batch_op:
        batch_op.drop_constraint('room_night_approval_room_night_request_fkey', type_='foreignkey')
        batch_op.create_foreign_key('room_night_approval_room_night_fkey', 'badge_to_room_night', ['room_night'], ['id'])

    op.drop_table('room_night_assignment')
    # ### end Alembic commands ###