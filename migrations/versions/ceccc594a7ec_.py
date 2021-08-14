"""empty message

Revision ID: ceccc594a7ec
Revises: d40ad95b8164
Create Date: 2021-08-14 22:54:39.437788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ceccc594a7ec'
down_revision = 'd40ad95b8164'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('questions', sa.Column('activant_answer_id', sa.Integer(), nullable=True))
    op.alter_column('questions', 'activant',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.create_foreign_key(None, 'questions', 'possible_answers', ['activant_answer_id'], ['id'])
    op.drop_column('questions', 'actiovant_answer_id')
    op.add_column('users', sa.Column('first_name', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('last_name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.add_column('questions', sa.Column('actiovant_answer_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'questions', type_='foreignkey')
    op.create_foreign_key(None, 'questions', 'possible_answers', ['actiovant_answer_id'], ['id'])
    op.alter_column('questions', 'activant',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_column('questions', 'activant_answer_id')
    # ### end Alembic commands ###