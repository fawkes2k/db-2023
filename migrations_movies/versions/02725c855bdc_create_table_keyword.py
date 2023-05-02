"""

create_table_keyword

Revision ID: 02725c855bdc
Creation date: 2023-05-02 15:19:13.686330

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = '02725c855bdc'
down_revision = '0d9ad78e15f7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE keyword(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);""")

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS keyword CASCADE;")
