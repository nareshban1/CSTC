# Generated by Django 3.1.2 on 2020-10-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_remove_subscription_renewdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='InstallDate',
            field=models.DateField(),
        ),
    ]
