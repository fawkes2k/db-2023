"""

create_table_movie_company

Revision ID: 0d9ad78e15f7
Creation date: 2023-05-02 15:18:58.292487

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = '0d9ad78e15f7'
down_revision = '8b0c674e7c12'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE movie_company(
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    company_id INT REFERENCES pcompany(id) ON DELETE CASCADE
);""")

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS movie_company CASCADE;")
