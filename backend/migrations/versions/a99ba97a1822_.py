"""empty message

Revision ID: a99ba97a1822
Revises: 69b7ba15c7d4
Create Date: 2022-12-11 15:30:18.050408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a99ba97a1822'
down_revision = '69b7ba15c7d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post_liker',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['Post.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_liker')
    # ### end Alembic commands ###
