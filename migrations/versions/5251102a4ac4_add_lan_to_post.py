"""add lan to post

Revision ID: 5251102a4ac4
Revises: c39ccd29fff2
Create Date: 2021-06-21 21:18:05.045770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5251102a4ac4'
down_revision = 'c39ccd29fff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
