# Generated by Django 3.1.6 on 2021-02-11 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meme', '0005_auto_20210211_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(),
        ),
    ]
