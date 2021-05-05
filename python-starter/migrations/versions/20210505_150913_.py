"""empty message

Revision ID: 7e6d30281d0d
Revises: d270a893856b
Create Date: 2021-05-05 15:09:13.568727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e6d30281d0d'
down_revision = 'd270a893856b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trades', sa.Column('makerCurrencyId', sa.Integer(), nullable=False))
    op.add_column('trades', sa.Column('takerCurrencyId', sa.Integer(), nullable=False))
    op.drop_constraint('unique_trade', 'trades', type_='unique')
    op.create_unique_constraint('unique_trade', 'trades', ['makerId', 'takerId', 'makerCurrencyId', 'takerCurrencyId', 'created_on'])
    op.drop_constraint('trades_currencyId_fkey', 'trades', type_='foreignkey')
    op.create_foreign_key(None, 'trades', 'currencies', ['makerCurrencyId'], ['id'])
    op.create_foreign_key(None, 'trades', 'currencies', ['takerCurrencyId'], ['id'])
    op.drop_column('trades', 'currencyId')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trades', sa.Column('currencyId', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'trades', type_='foreignkey')
    op.drop_constraint(None, 'trades', type_='foreignkey')
    op.create_foreign_key('trades_currencyId_fkey', 'trades', 'currencies', ['currencyId'], ['id'])
    op.drop_constraint('unique_trade', 'trades', type_='unique')
    op.create_unique_constraint('unique_trade', 'trades', ['makerId', 'takerId', 'currencyId', 'created_on'])
    op.drop_column('trades', 'takerCurrencyId')
    op.drop_column('trades', 'makerCurrencyId')
    # ### end Alembic commands ###
