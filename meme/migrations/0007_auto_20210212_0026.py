# Generated by Django 3.1.6 on 2021-02-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meme', '0006_auto_20210212_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
