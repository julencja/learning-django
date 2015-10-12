# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('foo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foo',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 12, 8, 46, 26, 471155, tzinfo=utc), verbose_name=b'date added'),
            preserve_default=False,
        ),
    ]
