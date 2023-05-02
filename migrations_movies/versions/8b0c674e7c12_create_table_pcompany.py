"""

create_table_pcompany

Revision ID: 8b0c674e7c12
Creation date: 2023-05-02 15:18:39.745069

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = '8b0c674e7c12'
down_revision = 'faffd9617ca6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE pcompany(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);""")

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS pcompany CASCADE;")
