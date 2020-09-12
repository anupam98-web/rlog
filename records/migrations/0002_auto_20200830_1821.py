# Generated by Django 3.1 on 2020-08-30 12:51

from django.db import migrations, models
import records.validators


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staging',
            name='contact_details_mobile',
            field=models.IntegerField(null=True, validators=[records.validators.phone_len]),
        ),
        migrations.AlterField(
            model_name='staging',
            name='contact_details_phone2',
            field=models.IntegerField(null=True, validators=[records.validators.phone_len]),
        ),
        migrations.AlterField(
            model_name='staging',
            name='position',
            field=models.TextField(null=True, validators=[records.validators.alnum]),
        ),
    ]
