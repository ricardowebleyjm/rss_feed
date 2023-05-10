"""First migration

Revision ID: 03170f2798de
Revises: 
Create Date: 2023-05-10 16:24:41.584087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03170f2798de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news_feed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_news_feed_id'), 'news_feed', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_news_feed_id'), table_name='news_feed')
    op.drop_table('news_feed')
    # ### end Alembic commands ###
