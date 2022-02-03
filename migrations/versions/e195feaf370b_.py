"""empty message

Revision ID: e195feaf370b
Revises: a0aa667de647
Create Date: 2022-02-02 19:09:16.618820

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e195feaf370b'
down_revision = 'a0aa667de647'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('car',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.Column('ano', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('car')
    # ### end Alembic commands ###
