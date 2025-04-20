# backend/app/db/migrations/versions/2024_06_01_initial.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'danang_properties',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('title', sa.String(255)),
        sa.Column('price', sa.Float()),
        sa.Column('area', sa.Float()),
        sa.Column('district', sa.String(50)),
        sa.Column('latitude', sa.Float()),
        sa.Column('longitude', sa.Float()),
        sa.Column('features', sa.JSON()),
        sa.Column('scraped_at', sa.DateTime(timezone=True))
    )

def downgrade():
    op.drop_table('danang_properties')
