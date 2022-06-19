"""empty message

Revision ID: c835b6b07d5f
Revises: 36b173e290ef
Create Date: 2022-06-19 13:07:49.627877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c835b6b07d5f'
down_revision = '36b173e290ef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Settings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('theme_path', sa.String(length=255), server_default='/', nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Settings', schema=None) as batch_op:
        batch_op.drop_column('theme_path')

    # ### end Alembic commands ###