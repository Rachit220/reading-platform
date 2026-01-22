from alembic import op
import sqlalchemy as sa

revision = "001"
down_revision = None

def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, unique=True),
        sa.Column("password", sa.String),
    )

def downgrade():
    op.drop_table("users")
