"""empty message

Revision ID: 8964ced32de0
Revises: 7409eac83319
Create Date: 2021-08-17 12:36:17.159803

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8964ced32de0'
down_revision = '7409eac83319'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answers_to_questions', 'question_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_constraint(None, 'answers_to_questions', type_='foreignkey')
    op.create_foreign_key(None, 'answers_to_questions', 'quiz_answers', ['id'], ['id'])
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
    op.add_column('answers_to_questions', sa.Column('quiz_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'answers_to_questions', type_='foreignkey')
    op.create_foreign_key(None, 'answers_to_questions', 'quizzes', ['quiz_id'], ['id'])
    op.alter_column('answers_to_questions', 'question_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
