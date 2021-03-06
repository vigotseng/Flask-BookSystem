"""empty message

Revision ID: 1797cef2cd31
Revises: 743dafb878fb
Create Date: 2019-12-05 19:43:48.765762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1797cef2cd31'
down_revision = '743dafb878fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('_password', sa.String(length=128), nullable=False))
    op.add_column('users', sa.Column('username', sa.String(length=32), nullable=False))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'username')
    op.drop_column('users', '_password')
    # ### end Alembic commands ###
