# Generated by Django 3.1 on 2020-09-11 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapping',
            name='Mappings',
        ),
    ]
