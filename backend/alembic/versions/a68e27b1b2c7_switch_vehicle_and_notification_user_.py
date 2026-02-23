"""switch vehicle and notification user fks to profiles

Revision ID: a68e27b1b2c7
Revises: 129184723be2
Create Date: 2026-02-24 01:31:25.419580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a68e27b1b2c7'
down_revision: Union[str, None] = '129184723be2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint(
        "vehicles_owner_id_fkey",
        "vehicles",
        schema="vehicle",
        type_="foreignkey",
    )

    op.drop_constraint(
        "notifications_user_id_fkey",
        "notifications",
        schema="notification",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "fk_vehicle_vehicles_owner_id_profiles",
        source_table="vehicles",
        referent_table="profiles",
        local_cols=["owner_id"],
        remote_cols=["id"],
        source_schema="vehicle",
        referent_schema="app_user",
        ondelete="CASCADE",
    )

    op.create_foreign_key(
        "fk_notification_notifications_user_id_profiles",
        source_table="notifications",
        referent_table="profiles",
        local_cols=["user_id"],
        remote_cols=["id"],
        source_schema="notification",
        referent_schema="app_user",
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint(
        "fk_notification_notifications_user_id_profiles",
        "notifications",
        schema="notification",
        type_="foreignkey",
    )

    op.drop_constraint(
        "fk_vehicle_vehicles_owner_id_profiles",
        "vehicles",
        schema="vehicle",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "vehicles_owner_id_fkey",
        source_table="vehicles",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        source_schema="vehicle",
        referent_schema="app_user",
        ondelete="CASCADE",
    )

    op.create_foreign_key(
        "notifications_user_id_fkey",
        source_table="notifications",
        referent_table="users",
        local_cols=["user_id"],
        remote_cols=["id"],
        source_schema="notification",
        referent_schema="app_user",
        ondelete="CASCADE",
    )
