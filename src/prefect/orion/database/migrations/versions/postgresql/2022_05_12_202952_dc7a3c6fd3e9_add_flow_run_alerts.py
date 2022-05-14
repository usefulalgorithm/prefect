"""Add flow run alert policies

Revision ID: dc7a3c6fd3e9
Revises: 1c9390e2f9c6
Create Date: 2022-05-12 20:29:52.681522

"""
from alembic import op
import sqlalchemy as sa
import prefect


# revision identifiers, used by Alembic.
revision = "dc7a3c6fd3e9"
down_revision = "1c9390e2f9c6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "flow_run_alert_queue",
        sa.Column(
            "id",
            prefect.orion.utilities.database.UUID(),
            server_default=sa.text("(GEN_RANDOM_UUID())"),
            nullable=False,
        ),
        sa.Column(
            "created",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "flow_run_alert_policy_id",
            prefect.orion.utilities.database.UUID(),
            nullable=False,
        ),
        sa.Column(
            "flow_run_state_id", prefect.orion.utilities.database.UUID(), nullable=False
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_flow_run_alert_queue")),
    )
    op.create_index(
        op.f("ix_flow_run_alert_queue__updated"),
        "flow_run_alert_queue",
        ["updated"],
        unique=False,
    )
    op.create_table(
        "flow_run_alert_policy",
        sa.Column(
            "id",
            prefect.orion.utilities.database.UUID(),
            server_default=sa.text("(GEN_RANDOM_UUID())"),
            nullable=False,
        ),
        sa.Column(
            "created",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated",
            prefect.orion.utilities.database.Timestamp(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("is_active", sa.Boolean(), server_default="1", nullable=False),
        sa.Column(
            "state_names",
            prefect.orion.utilities.database.JSON(astext_type=sa.Text()),
            server_default="[]",
            nullable=False,
        ),
        sa.Column(
            "tags",
            prefect.orion.utilities.database.JSON(astext_type=sa.Text()),
            server_default="[]",
            nullable=False,
        ),
        sa.Column("message_template", sa.String(), nullable=True),
        sa.Column(
            "block_document_id", prefect.orion.utilities.database.UUID(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["block_document_id"],
            ["block_document.id"],
            name=op.f("fk_flow_run_alert_policy__block_document_id__block_document"),
            ondelete="cascade",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_flow_run_alert")),
    )
    op.create_index(
        op.f("ix_flow_run_alert_policy__name"),
        "flow_run_alert_policy",
        ["name"],
        unique=False,
    )
    op.create_index(
        op.f("ix_flow_run_alert_policy__updated"),
        "flow_run_alert_policy",
        ["updated"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_flow_run_alert_policy__name"),
        table_name="flow_run_alert_policy",
    )
    op.drop_index(
        op.f("ix_flow_run_alert_policy__updated"),
        table_name="flow_run_alert_policy",
    )
    op.drop_table("flow_run_alert_policy")
    op.drop_index(
        op.f("ix_flow_run_alert_queue__updated"),
        table_name="flow_run_alert_queue",
    )
    op.drop_table("flow_run_alert_queue")
    # ### end Alembic commands ###
