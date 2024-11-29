from piccolo.apps.migrations.auto.migration_manager import MigrationManager
from piccolo.columns.base import OnDelete
from piccolo.columns.base import OnUpdate
from piccolo.columns.column_types import Array
from piccolo.columns.column_types import Boolean
from piccolo.columns.column_types import ForeignKey
from piccolo.columns.column_types import Integer
from piccolo.columns.column_types import Serial
from piccolo.columns.column_types import Text
from piccolo.columns.column_types import UUID
from piccolo.columns.column_types import Varchar
from piccolo.columns.defaults.uuid import UUID4
from piccolo.columns.indexes import IndexMethod
from piccolo.table import Table


class KEmoji(Table, tablename="k_emoji", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class KFollows(Table, tablename="k_follows", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class KMailSettings(Table, tablename="k_mail_settings", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class KModerationSettings(Table, tablename="k_moderation_settings", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class KNote(Table, tablename="k_note", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class KReaction(Table, tablename="k_reaction", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class KS3Settings(Table, tablename="ks3_settings", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


class KUser(Table, tablename="k_user", schema=None):
    id = Serial(
        null=False,
        primary_key=True,
        unique=False,
        index=False,
        index_method=IndexMethod.btree,
        choices=None,
        db_column_name="id",
        secret=False,
    )


ID = "2024-11-29T18:05:45:222315"
VERSION = "1.22.0"
DESCRIPTION = ""


async def forwards():
    manager = MigrationManager(
        migration_id=ID, app_name="kagura", description=DESCRIPTION
    )

    manager.add_table(
        class_name="KIPLog", tablename="kip_log", schema=None, columns=None
    )

    manager.add_table(
        class_name="KModerationSettings",
        tablename="k_moderation_settings",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="KMailSettings",
        tablename="k_mail_settings",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="KS3Settings",
        tablename="ks3_settings",
        schema=None,
        columns=None,
    )

    manager.add_table(
        class_name="KSettings", tablename="k_settings", schema=None, columns=None
    )

    manager.add_table(
        class_name="KMedia", tablename="k_media", schema=None, columns=None
    )

    manager.add_table(
        class_name="KReport", tablename="k_report", schema=None, columns=None
    )

    manager.add_column(
        table_class_name="KIPLog",
        tablename="kip_log",
        column_name="id",
        db_column_name="id",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KIPLog",
        tablename="kip_log",
        column_name="user",
        db_column_name="user",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": "KUser",
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KIPLog",
        tablename="kip_log",
        column_name="ip_address",
        db_column_name="ip_address",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="id",
        db_column_name="id",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="rules",
        db_column_name="rules",
        column_class_name="Array",
        column_class=Array,
        params={
            "base_column": Text(
                default="",
                null=False,
                primary_key=False,
                unique=False,
                index=False,
                index_method=IndexMethod.btree,
                choices=None,
                db_column_name=None,
                secret=False,
            ),
            "default": list,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="open_registrations",
        db_column_name="open_registrations",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="mail_required",
        db_column_name="mail_required",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="disallow_email_domains",
        db_column_name="disallow_email_domains",
        column_class_name="Array",
        column_class=Array,
        params={
            "base_column": Text(
                default="",
                null=False,
                primary_key=False,
                unique=False,
                index=False,
                index_method=IndexMethod.btree,
                choices=None,
                db_column_name=None,
                secret=False,
            ),
            "default": list,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="reserved_names",
        db_column_name="reserved_names",
        column_class_name="Array",
        column_class=Array,
        params={
            "base_column": Text(
                default="",
                null=False,
                primary_key=False,
                unique=False,
                index=False,
                index_method=IndexMethod.btree,
                choices=None,
                db_column_name=None,
                secret=False,
            ),
            "default": list,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="muted_tags",
        db_column_name="muted_tags",
        column_class_name="Array",
        column_class=Array,
        params={
            "base_column": Text(
                default="",
                null=False,
                primary_key=False,
                unique=False,
                index=False,
                index_method=IndexMethod.btree,
                choices=None,
                db_column_name=None,
                secret=False,
            ),
            "default": list,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="muted_servers",
        db_column_name="muted_servers",
        column_class_name="Array",
        column_class=Array,
        params={
            "base_column": Text(
                default="",
                null=False,
                primary_key=False,
                unique=False,
                index=False,
                index_method=IndexMethod.btree,
                choices=None,
                db_column_name=None,
                secret=False,
            ),
            "default": list,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="blocked_servers",
        db_column_name="blocked_servers",
        column_class_name="Array",
        column_class=Array,
        params={
            "base_column": Text(
                default="",
                null=False,
                primary_key=False,
                unique=False,
                index=False,
                index_method=IndexMethod.btree,
                choices=None,
                db_column_name=None,
                secret=False,
            ),
            "default": list,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="use_mcaptcha",
        db_column_name="use_mcaptcha",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="mcaptcha_instance",
        db_column_name="mcaptcha_instance",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="mcaptcha_site_key",
        db_column_name="mcaptcha_site_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="mcaptcha_secret_key",
        db_column_name="mcaptcha_secret_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="use_turnstile",
        db_column_name="use_turnstile",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="turnstile_site_key",
        db_column_name="turnstile_site_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="turnstile_secret_key",
        db_column_name="turnstile_secret_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="use_hcaptcha",
        db_column_name="use_hcaptcha",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="hcaptcha_site_key",
        db_column_name="hcaptcha_site_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="hcaptcha_secret_key",
        db_column_name="hcaptcha_secret_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="use_recaptcha",
        db_column_name="use_recaptcha",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="recaptcha_site_key",
        db_column_name="recaptcha_site_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="recaptcha_secret_key",
        db_column_name="recaptcha_secret_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KModerationSettings",
        tablename="k_moderation_settings",
        column_name="logging_ip",
        db_column_name="logging_ip",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMailSettings",
        tablename="k_mail_settings",
        column_name="id",
        db_column_name="id",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMailSettings",
        tablename="k_mail_settings",
        column_name="enable_email",
        db_column_name="enable_email",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMailSettings",
        tablename="k_mail_settings",
        column_name="address",
        db_column_name="address",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMailSettings",
        tablename="k_mail_settings",
        column_name="host",
        db_column_name="host",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMailSettings",
        tablename="k_mail_settings",
        column_name="port",
        db_column_name="port",
        column_class_name="Integer",
        column_class=Integer,
        params={
            "default": 465,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMailSettings",
        tablename="k_mail_settings",
        column_name="username",
        db_column_name="username",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMailSettings",
        tablename="k_mail_settings",
        column_name="password",
        db_column_name="password",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMailSettings",
        tablename="k_mail_settings",
        column_name="use_ssl",
        db_column_name="use_ssl",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": True,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="id",
        db_column_name="id",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="use_s3",
        db_column_name="use_s3",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="base_url",
        db_column_name="base_url",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="bucket",
        db_column_name="bucket",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="prefix",
        db_column_name="prefix",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="endpoint",
        db_column_name="endpoint",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="region",
        db_column_name="region",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "us-east-1",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="access_key",
        db_column_name="access_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="secret_key",
        db_column_name="secret_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="use_ssl",
        db_column_name="use_ssl",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="use_proxy",
        db_column_name="use_proxy",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="public_read_on_upload",
        db_column_name="public_read_on_upload",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KS3Settings",
        tablename="ks3_settings",
        column_name="s3_force_path_style",
        db_column_name="s3_force_path_style",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="id",
        db_column_name="id",
        column_class_name="UUID",
        column_class=UUID,
        params={
            "default": UUID4(),
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="name",
        db_column_name="name",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="description",
        db_column_name="description",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="icon_url",
        db_column_name="icon_url",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="icon_192_url",
        db_column_name="icon_192_url",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="icon_512_url",
        db_column_name="icon_512_url",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="repository_url",
        db_column_name="repository_url",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "https://github.com/kagura-soc/kagura",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="issue_url",
        db_column_name="issue_url",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "https://github.com/kagura-soc/kagura/issues",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="s3",
        db_column_name="s3",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": KS3Settings,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="moderation",
        db_column_name="moderation",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": KModerationSettings,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KSettings",
        tablename="k_settings",
        column_name="smtp",
        db_column_name="smtp",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": KMailSettings,
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMedia",
        tablename="k_media",
        column_name="id",
        db_column_name="id",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMedia",
        tablename="k_media",
        column_name="filename",
        db_column_name="filename",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMedia",
        tablename="k_media",
        column_name="path",
        db_column_name="path",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": None,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMedia",
        tablename="k_media",
        column_name="url",
        db_column_name="url",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": None,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMedia",
        tablename="k_media",
        column_name="filesize",
        db_column_name="filesize",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMedia",
        tablename="k_media",
        column_name="owner",
        db_column_name="owner",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "related_name": "media",
            "references": "KUser",
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KMedia",
        tablename="k_media",
        column_name="notes",
        db_column_name="notes",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "related_name": "media",
            "references": "KNote",
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KReport",
        tablename="k_report",
        column_name="id",
        db_column_name="id",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": True,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KReport",
        tablename="k_report",
        column_name="note_id",
        db_column_name="note_id",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": None,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KReport",
        tablename="k_report",
        column_name="user_id",
        db_column_name="user_id",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": None,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KReport",
        tablename="k_report",
        column_name="reason",
        db_column_name="reason",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KReport",
        tablename="k_report",
        column_name="is_resolved",
        db_column_name="is_resolved",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KNote",
        tablename="k_note",
        column_name="cw",
        db_column_name="cw",
        column_class_name="Varchar",
        column_class=Varchar,
        params={
            "length": 100,
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KNote",
        tablename="k_note",
        column_name="media",
        db_column_name="media",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": "Media",
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KNote",
        tablename="k_note",
        column_name="original",
        db_column_name="original",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": "KNote",
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KNote",
        tablename="k_note",
        column_name="reply",
        db_column_name="reply",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": "KNote",
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="host",
        db_column_name="host",
        column_class_name="ForeignKey",
        column_class=ForeignKey,
        params={
            "references": "KHost",
            "on_delete": OnDelete.cascade,
            "on_update": OnUpdate.cascade,
            "target_column": None,
            "null": True,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="is_muted",
        db_column_name="is_muted",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="is_suspended",
        db_column_name="is_suspended",
        column_class_name="Boolean",
        column_class=Boolean,
        params={
            "default": False,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="private_key",
        db_column_name="private_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": None,
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="public_key",
        db_column_name="public_key",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.add_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="totp_seed",
        db_column_name="totp_seed",
        column_class_name="Text",
        column_class=Text,
        params={
            "default": "",
            "null": False,
            "primary_key": False,
            "unique": False,
            "index": False,
            "index_method": IndexMethod.btree,
            "choices": None,
            "db_column_name": None,
            "secret": False,
        },
        schema=None,
    )

    manager.alter_column(
        table_class_name="KNote",
        tablename="k_note",
        column_name="user",
        db_column_name="user",
        params={"references": KUser},
        old_params={"references": KUser},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KReaction",
        tablename="k_reaction",
        column_name="user",
        db_column_name="user",
        params={"references": KUser},
        old_params={"references": KUser},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KReaction",
        tablename="k_reaction",
        column_name="note",
        db_column_name="note",
        params={"references": KNote},
        old_params={"references": KNote},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KReaction",
        tablename="k_reaction",
        column_name="emoji",
        db_column_name="emoji",
        params={"references": KEmoji},
        old_params={"references": KEmoji},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KHost",
        tablename="k_host",
        column_name="users",
        db_column_name="users",
        params={"references": KUser},
        old_params={"references": KUser},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="followers",
        db_column_name="followers",
        params={"references": KFollows},
        old_params={"references": KFollows},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="following",
        db_column_name="following",
        params={"references": KFollows},
        old_params={"references": KFollows},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="notes",
        db_column_name="notes",
        params={"references": KNote},
        old_params={"references": KNote},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KUser",
        tablename="k_user",
        column_name="reactions",
        db_column_name="reactions",
        params={"references": KReaction},
        old_params={"references": KReaction},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KFollows",
        tablename="k_follows",
        column_name="followee",
        db_column_name="followee",
        params={"references": KUser},
        old_params={"references": KUser},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    manager.alter_column(
        table_class_name="KFollows",
        tablename="k_follows",
        column_name="follower",
        db_column_name="follower",
        params={"references": KUser},
        old_params={"references": KUser},
        column_class=ForeignKey,
        old_column_class=ForeignKey,
        schema=None,
    )

    return manager
