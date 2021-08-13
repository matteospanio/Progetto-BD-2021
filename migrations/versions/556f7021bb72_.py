"""empty message

Revision ID: 556f7021bb72
Revises: 97c823195ed5
Create Date: 2021-08-13 16:27:26.091382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '556f7021bb72'
down_revision = '97c823195ed5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('questions', 'activant',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_constraint('questions_activable_question_fkey', 'questions', type_='foreignkey')
    op.drop_constraint('questions_activant_answer_id_fkey', 'questions', type_='foreignkey')
    op.drop_constraint('questions_type_id_fkey', 'questions', type_='foreignkey')
    op.drop_constraint('questions_category_id_fkey', 'questions', type_='foreignkey')
    op.drop_column('questions', 'type_id')
    op.drop_column('questions', 'category_id')
    op.drop_column('questions', 'activable_question')
    op.drop_column('questions', 'activant_answer_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('activant_answer_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('questions', sa.Column('activable_question', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('questions', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('questions', sa.Column('type_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('questions_category_id_fkey', 'questions', 'questions_category', ['category_id'], ['id'])
    op.create_foreign_key('questions_type_id_fkey', 'questions', 'questions_type', ['type_id'], ['id'])
    op.create_foreign_key('questions_activant_answer_id_fkey', 'questions', 'possible_answers', ['activant_answer_id'], ['id'])
    op.create_foreign_key('questions_activable_question_fkey', 'questions', 'questions', ['activable_question'], ['id'])
    op.alter_column('questions', 'activant',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###