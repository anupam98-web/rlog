# Generated by Django 3.1 on 2020-09-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_staging_reason'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staging',
            name='current_salary',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='staging',
            name='expected_salary_amt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='staging',
            name='expected_salary_percentage',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='staging',
            name='total_exp',
            field=models.TextField(null=True),
        ),
    ]
