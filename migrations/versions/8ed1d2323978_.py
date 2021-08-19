"""empty message

Revision ID: 8ed1d2323978
Revises: 604fa8a5b404
Create Date: 2021-08-18 19:08:38.399698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ed1d2323978'
down_revision = '604fa8a5b404'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('have_as_answer', sa.Column('possible_answer_id', sa.Integer(), nullable=False))
    op.add_column('have_as_answer', sa.Column('answer_to_questions_id', sa.Integer(), nullable=False))
    op.drop_constraint('have_as_answer_possible_answers_id_fkey', 'have_as_answer', type_='foreignkey')
    op.create_foreign_key('fk_possible_answers', 'have_as_answer', 'possible_answers', ['possible_answer_id'], ['id'])
    op.create_foreign_key('fk_answer_to_questions', 'have_as_answer', 'answers_to_questions', ['answer_to_questions_id', 'question_id'], ['id', 'question_id'])
    op.drop_column('have_as_answer', 'possible_answers_id')
    op.drop_column('have_as_answer', 'answers_to_questions_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('have_as_answer', sa.Column('answers_to_questions_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('have_as_answer', sa.Column('possible_answers_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint('fk_answer_to_questions', 'have_as_answer', type_='foreignkey')
    op.drop_constraint('fk_possible_answers', 'have_as_answer', type_='foreignkey')
    op.create_foreign_key('have_as_answer_possible_answers_id_fkey', 'have_as_answer', 'possible_answers', ['possible_answers_id'], ['id'])
    op.drop_column('have_as_answer', 'answer_to_questions_id')
    op.drop_column('have_as_answer', 'possible_answer_id')
    # ### end Alembic commands ###
