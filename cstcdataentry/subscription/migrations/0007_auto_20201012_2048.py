# Generated by Django 3.1.2 on 2020-10-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0006_auto_20201012_2044'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='TotalAmount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='Installation_number',
            field=models.IntegerField(default=1),
        ),
    ]
