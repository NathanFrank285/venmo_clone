"""empty message

Revision ID: 8d000b7ee8c0
Revises: 28b2ea2a81fe
Create Date: 2021-05-11 16:32:36.981623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d000b7ee8c0'
down_revision = '28b2ea2a81fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('live', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'live')
    # ### end Alembic commands ###