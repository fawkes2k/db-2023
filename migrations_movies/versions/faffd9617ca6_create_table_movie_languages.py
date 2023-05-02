"""

create table movie_languages

Revision ID: faffd9617ca6
Creation date: 2023-05-02 13:20:47.857449

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'faffd9617ca6'
down_revision = 'bd05c39d2dca'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE movie_language(
    movie_id INT REFERENCES movies(movie_id) ON DELETE CASCADE,
    iso_639_1 TEXT REFERENCES language(iso_639_1) ON DELETE CASCADE
    );""")

def downgrade() -> None:
    op.execute("""DROP TABLE IF EXISTS movie_language CASCADE;""")
