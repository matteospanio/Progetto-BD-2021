"""empty message

Revision ID: e4528958640e
Revises: f519a99802af
Create Date: 2021-08-18 17:57:56.874976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4528958640e'
down_revision = 'f519a99802af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('have_as_answer',
    sa.Column('possible_answer_id', sa.Integer(), nullable=False),
    sa.Column('answer_to_questions_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['answer_to_questions_id', 'question_id'], ['answers_to_questions.id', 'answers_to_questions.question_id'], name='fk_answer_to_questions'),
    sa.ForeignKeyConstraint(['possible_answer_id'], ['possible_answers.id'], name='fk_possible_answers'),
    sa.PrimaryKeyConstraint('possible_answer_id', 'answer_to_questions_id', 'question_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('have_as_answer')
    # ### end Alembic commands ###
