"""empty message

Revision ID: 69b7ba15c7d4
Revises: ff701eb86c4a
Create Date: 2022-11-16 22:14:15.512934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69b7ba15c7d4'
down_revision = 'ff701eb86c4a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Post', sa.Column('image', sa.String(length=255), nullable=True))
    op.add_column('User', sa.Column('image', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('User', 'image')
    op.drop_column('Post', 'image')
    # ### end Alembic commands ###
