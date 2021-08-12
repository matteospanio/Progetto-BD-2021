"""empty message

Revision ID: 97c823195ed5
Revises: 9ef547a5b087
Create Date: 2021-08-11 23:46:59.535180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97c823195ed5'
down_revision = '9ef547a5b087'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('activant_answer_id', sa.Integer(), nullable=True))
    op.drop_constraint('questions_actiovant_answer_id_fkey', 'questions', type_='foreignkey')
    op.create_foreign_key(None, 'questions', 'possible_answers', ['activant_answer_id'], ['id'])
    op.drop_column('questions', 'actiovant_answer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('actiovant_answer_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.create_foreign_key('questions_actiovant_answer_id_fkey', 'questions', 'possible_answers', ['actiovant_answer_id'], ['id'])
    op.drop_column('questions', 'activant_answer_id')
    # ### end Alembic commands ###