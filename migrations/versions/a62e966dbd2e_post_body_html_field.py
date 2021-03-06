"""Post body_html field

Revision ID: a62e966dbd2e
Revises: 0de5aaa2b064
Create Date: 2017-11-21 12:49:38.270587

"""

# revision identifiers, used by Alembic.
revision = 'a62e966dbd2e'
down_revision = '0de5aaa2b064'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
