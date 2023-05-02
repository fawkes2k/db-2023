"""

create_table_movie_keyword

Revision ID: ba7f3771f951
Creation date: 2023-05-02 15:19:36.037449

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'ba7f3771f951'
down_revision = '02725c855bdc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE movie_keyword(
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    keyword_id INT REFERENCES keyword(id) ON DELETE CASCADE
);""")

def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS movie_keyword CASCADE;")
