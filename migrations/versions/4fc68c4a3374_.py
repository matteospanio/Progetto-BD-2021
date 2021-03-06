"""empty message

Revision ID: 4fc68c4a3374
Revises: ed9530ef324a
Create Date: 2021-08-28 11:33:25.374548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fc68c4a3374'
down_revision = 'ed9530ef324a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('quiz_answers', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'quiz_answers', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'quiz_answers', type_='foreignkey')
    op.drop_column('quiz_answers', 'user_id')
    # ### end Alembic commands ###
