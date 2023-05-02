"""

create_table_languages

Revision ID: bd05c39d2dca
Creation date: 2023-05-02 12:07:53.089704

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'bd05c39d2dca'
down_revision = '03a94830a8ac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE language(
        iso_639_1 TEXT PRIMARY KEY,
        name TEXT NOT NULL
    );""")

def downgrade() -> None:
    op.execute("""DROP TABLE IF EXISTS language CASCADE;""")
