"""Add Aquarium, UserAquarium, WaterParameter, Post, and Comment models along with relationships

Revision ID: 4487d836f00f
Revises: c24fbe99dd66
Create Date: 2023-06-21 17:07:44.757333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4487d836f00f'
down_revision = 'c24fbe99dd66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('aquariums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=120), nullable=True),
    sa.Column('volume', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_aquariums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('aquarium_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['aquarium_id'], ['aquariums.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'aquarium_id', name='uq_user_aquarium')
    )
    op.create_table('water_parameters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('aquarium_id', sa.Integer(), nullable=True),
    sa.Column('ph', sa.Float(), nullable=True),
    sa.Column('ammonia', sa.Float(), nullable=True),
    sa.Column('nitrite', sa.Float(), nullable=True),
    sa.Column('nitrate', sa.Float(), nullable=True),
    sa.Column('phosphate', sa.Float(), nullable=True),
    sa.Column('calcium', sa.Float(), nullable=True),
    sa.Column('magnesium', sa.Float(), nullable=True),
    sa.Column('alkalinity', sa.Float(), nullable=True),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['aquarium_id'], ['aquariums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('water_parameters')
    op.drop_table('user_aquariums')
    op.drop_table('comments')
    op.drop_table('posts')
    op.drop_table('aquariums')
    # ### end Alembic commands ###
