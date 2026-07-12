"""Link assets with security scans

Revision ID: 88142bf7d343
Revises: a4f785c23906
Create Date: 2026-07-12 19:01:01.891718
"""

from alembic import op
import sqlalchemy as sa

revision = "88142bf7d343"
down_revision = "a4f785c23906"
branch_labels = None
depends_on = None


def upgrade():

    with op.batch_alter_table("security_scans") as batch_op:

        batch_op.add_column(
            sa.Column("asset_id", sa.Integer(), nullable=True)
        )

        batch_op.create_foreign_key(
            "fk_security_scans_asset_id",   # <-- Give the FK a name
            "assets",
            ["asset_id"],
            ["id"]
        )


def downgrade():

    with op.batch_alter_table("security_scans") as batch_op:

        batch_op.drop_constraint(
            "fk_security_scans_asset_id",
            type_="foreignkey"
        )

        batch_op.drop_column("asset_id")