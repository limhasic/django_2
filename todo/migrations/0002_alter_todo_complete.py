# Generated by Django 3.2.16 on 2023-02-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
