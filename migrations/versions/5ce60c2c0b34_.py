"""empty message

Revision ID: 5ce60c2c0b34
Revises: 
Create Date: 2022-05-05 23:06:09.722029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ce60c2c0b34'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Languages', schema=None) as batch_op:
        batch_op.add_column(sa.Column('test', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Languages', schema=None) as batch_op:
        batch_op.drop_column('test')

    # ### end Alembic commands ###
