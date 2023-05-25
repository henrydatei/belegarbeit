# Generated by Django 4.2.1 on 2023-05-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_profile_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contract_end_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contract_start_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='hours_per_week',
            field=models.FloatField(default=0),
        ),
    ]
