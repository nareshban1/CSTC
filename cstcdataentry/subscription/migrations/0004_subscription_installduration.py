# Generated by Django 3.1.2 on 2020-10-10 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_auto_20201010_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='InstallDuration',
            field=models.IntegerField(default=1),
        ),
    ]
