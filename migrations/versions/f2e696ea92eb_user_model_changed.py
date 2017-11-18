"""User model changed

Revision ID: f2e696ea92eb
Revises: 953467c2c5ed
Create Date: 2017-11-18 12:23:34.015224

"""

# revision identifiers, used by Alembic.
revision = 'f2e696ea92eb'
down_revision = '953467c2c5ed'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
