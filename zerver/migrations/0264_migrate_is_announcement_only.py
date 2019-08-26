# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-01-25 23:47
from __future__ import unicode_literals

from django.db import migrations
from django.db.backends.postgresql_psycopg2.schema import DatabaseSchemaEditor
from django.db.migrations.state import StateApps


def upgrade_stream_post_policy(apps: StateApps, schema_editor: DatabaseSchemaEditor) -> None:
    STREAM_POST_POLICY_EVERYONE = 1
    STREAM_POST_POLICY_ADMINS = 2

    Stream = apps.get_model('zerver', 'Stream')
    Stream.objects.filter(is_announcement_only=False) \
        .update(stream_post_policy=STREAM_POST_POLICY_EVERYONE)
    Stream.objects.filter(is_announcement_only=True) \
        .update(stream_post_policy=STREAM_POST_POLICY_ADMINS)

class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0263_stream_stream_post_policy'),
    ]

    operations = [
        migrations.RunPython(upgrade_stream_post_policy,
                             reverse_code=migrations.RunPython.noop),
    ]