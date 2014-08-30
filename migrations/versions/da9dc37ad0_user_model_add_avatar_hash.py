"""User model add avatar hash

Revision ID: da9dc37ad0
Revises: 59c28599194
Create Date: 2014-08-28 16:12:02.171706

"""

# revision identifiers, used by Alembic.
revision = 'da9dc37ad0'
down_revision = '59c28599194'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar_hash', sa.String(length=32), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar_hash')
    ### end Alembic commands ###
