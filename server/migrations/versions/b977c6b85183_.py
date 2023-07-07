"""empty message

Revision ID: b977c6b85183
Revises: 
Create Date: 2023-07-07 11:30:54.771478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b977c6b85183'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('continents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('language', sa.String(), nullable=False),
    sa.Column('continent_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['continent_id'], ['continents.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('restaurant_recommendation', sa.String(), nullable=False),
    sa.Column('city_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['cities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('foods')
    op.drop_table('cities')
    op.drop_table('continents')
    # ### end Alembic commands ###