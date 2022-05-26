"""empty message

Revision ID: b2a7a08c6b7f
Revises: a313ee108ec2
Create Date: 2022-05-26 17:22:08.952979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b2a7a08c6b7f'
down_revision = 'a313ee108ec2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Language', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language_code', sa.String(), server_default='en', nullable=False))
        batch_op.drop_column('language')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Language', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.VARCHAR(), server_default=sa.text("'en'"), nullable=False))
        batch_op.drop_column('language_code')

    # ### end Alembic commands ###
