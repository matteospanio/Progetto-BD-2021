"""empty message

Revision ID: dbf03ac3f199
Revises: ce0165d64d91
Create Date: 2021-08-29 15:47:41.185379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbf03ac3f199'
down_revision = 'ce0165d64d91'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('answers_to_questions_id_fkey', 'answers_to_questions', type_='foreignkey')
    op.drop_constraint('answers_to_questions_question_id_fkey', 'answers_to_questions', type_='foreignkey')
    op.create_foreign_key(None, 'answers_to_questions', 'quiz_answers', ['id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'answers_to_questions', 'questions', ['question_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('fk_possible_answers', 'have_as_answer', type_='foreignkey')
    op.drop_constraint('fk_answer_to_questions', 'have_as_answer', type_='foreignkey')
    op.create_foreign_key('fk_possible_answers', 'have_as_answer', 'possible_answers', ['possible_answer_id'], ['id'], ondelete='SET NULL')
    op.create_foreign_key('fk_answer_to_questions', 'have_as_answer', 'answers_to_questions', ['answer_to_questions_id', 'question_id'], ['id', 'question_id'], ondelete='SET NULL')
    op.drop_constraint('possible_answers_question_id_fkey', 'possible_answers', type_='foreignkey')
    op.create_foreign_key(None, 'possible_answers', 'questions', ['question_id'], ['id'], ondelete='CASCADE')
    op.drop_column('possible_answers', 'text_html')
    op.drop_constraint('questions_quiz_id_fkey', 'questions', type_='foreignkey')
    op.drop_constraint('questions_activated_by_fkey', 'questions', type_='foreignkey')
    op.create_foreign_key(None, 'questions', 'questions', ['activated_by'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'questions', 'quizzes', ['quiz_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('quiz_answers_quiz_id_fkey', 'quiz_answers', type_='foreignkey')
    op.create_foreign_key(None, 'quiz_answers', 'quizzes', ['quiz_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'quiz_answers', type_='foreignkey')
    op.create_foreign_key('quiz_answers_quiz_id_fkey', 'quiz_answers', 'quizzes', ['quiz_id'], ['id'])
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.create_foreign_key('questions_activated_by_fkey', 'questions', 'questions', ['activated_by'], ['id'])
    op.create_foreign_key('questions_quiz_id_fkey', 'questions', 'quizzes', ['quiz_id'], ['id'])
    op.add_column('possible_answers', sa.Column('text_html', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'possible_answers', type_='foreignkey')
    op.create_foreign_key('possible_answers_question_id_fkey', 'possible_answers', 'questions', ['question_id'], ['id'])
    op.drop_constraint('fk_answer_to_questions', 'have_as_answer', type_='foreignkey')
    op.drop_constraint('fk_possible_answers', 'have_as_answer', type_='foreignkey')
    op.create_foreign_key('fk_answer_to_questions', 'have_as_answer', 'answers_to_questions', ['answer_to_questions_id', 'question_id'], ['id', 'question_id'])
    op.create_foreign_key('fk_possible_answers', 'have_as_answer', 'possible_answers', ['possible_answer_id'], ['id'])
    op.drop_constraint(None, 'answers_to_questions', type_='foreignkey')
    op.drop_constraint(None, 'answers_to_questions', type_='foreignkey')
    op.create_foreign_key('answers_to_questions_question_id_fkey', 'answers_to_questions', 'questions', ['question_id'], ['id'])
    op.create_foreign_key('answers_to_questions_id_fkey', 'answers_to_questions', 'quiz_answers', ['id'], ['id'])
    # ### end Alembic commands ###