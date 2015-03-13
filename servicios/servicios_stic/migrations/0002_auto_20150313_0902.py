# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import servicios_stic.models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios_stic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='imagefile',
            field=models.FileField(default=datetime.datetime(2015, 3, 13, 9, 2, 13, 497657, tzinfo=utc), upload_to=servicios_stic.models.content_image_name),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=servicios_stic.models.content_file_name),
            preserve_default=True,
        ),
    ]
