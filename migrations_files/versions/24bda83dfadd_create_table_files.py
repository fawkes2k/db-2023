"""create table files

Revision ID: 24bda83dfadd
Revises: 
Create Date: 2023-05-26 22:45:58.323952

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '24bda83dfadd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""CREATE TABLE files(
        file_id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        bytes INT NOT NULL CHECK(bytes >= 0),
        depth INT NOT NULL CHECK(depth >= 0),
        accessed TIMESTAMP NOT NULL,
        modified TIMESTAMP NOT NULL,
        basename TEXT NOT NULL,
        extension TEXT CHECK(extension LIKE '.%'),
        type TEXT NOT NULL CHECK(type = 'f' OR type = 'd'),
        mode TEXT NOT NULL CHECK(mode LIKE '[d-]([r-][w-][x-]){3}'),
        parent_text TEXT NOT NULL,
        full_path TEXT NOT NULL CHECK(full_path = parent_text || basename || extension)
    )""")


def downgrade() -> None:
    op.execute('DROP TABLE files CASCADE')