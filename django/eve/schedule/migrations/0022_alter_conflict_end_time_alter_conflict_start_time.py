# Generated by Django 4.1.2 on 2022-12-10 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0021_alter_conflict_end_time_alter_conflict_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conflict',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conflict',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
