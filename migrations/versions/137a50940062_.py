"""empty message

Revision ID: 137a50940062
Revises: dd46aa0fa07b
Create Date: 2021-08-17 09:37:31.725104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '137a50940062'
down_revision = 'dd46aa0fa07b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answers_to_questions', sa.Column('text_html', sa.Text(), nullable=True))
    op.drop_constraint('answers_to_questions_quiz_id_fkey', 'answers_to_questions', type_='foreignkey')
    op.drop_column('answers_to_questions', 'quiz_id')
    op.add_column('possible_answers', sa.Column('text_html', sa.Text(), nullable=True))
    op.add_column('questions', sa.Column('text_html', sa.Text(), nullable=True))
    op.add_column('quizzes', sa.Column('description_html', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('quizzes', 'description_html')
    op.drop_column('questions', 'text_html')
    op.drop_column('possible_answers', 'text_html')
    op.add_column('answers_to_questions', sa.Column('quiz_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('answers_to_questions_quiz_id_fkey', 'answers_to_questions', 'quizzes', ['quiz_id'], ['id'])
    op.drop_column('answers_to_questions', 'text_html')
    # ### end Alembic commands ###
