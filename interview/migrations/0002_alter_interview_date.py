# Generated by Django 4.2.16 on 2024-09-11 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("interview", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interview",
            name="date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 9, 11, 12, 54, 47, 129285, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
