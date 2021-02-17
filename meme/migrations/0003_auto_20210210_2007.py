# Generated by Django 3.1.6 on 2021-02-10 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meme', '0002_auto_20210209_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='cap',
            new_name='caption',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 10, 20, 7, 50, 691286)),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]