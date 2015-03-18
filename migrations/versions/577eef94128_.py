"""empty message

Revision ID: 577eef94128
Revises: 1df49594ea2
Create Date: 2015-03-17 17:10:15.662082

"""

# revision identifiers, used by Alembic.
revision = '577eef94128'
down_revision = '1df49594ea2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('project', sa.Column('group_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'project', 'group', ['group_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'project', type_='foreignkey')
    op.drop_column('project', 'group_id')
    op.drop_table('likes')
    ### end Alembic commands ###