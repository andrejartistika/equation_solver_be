# Generated by Django 2.2.5 on 2020-07-15 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mer', '0003_predictedphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mernn',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
