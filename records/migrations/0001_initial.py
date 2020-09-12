# Generated by Django 3.1 on 2020-08-23 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientName', models.TextField(null=True)),
                ('CreatedOn', models.DateField(null=True)),
                ('ShortName', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruiter', models.TextField(null=True)),
                ('client', models.TextField(null=True)),
                ('position', models.TextField(null=True)),
                ('reqt_date', models.DateField(null=True)),
                ('date_cv_submitted', models.DateField(null=True)),
                ('candidate_name', models.TextField(null=True)),
                ('current_status', models.IntegerField(null=True)),
                ('current_status_desc', models.TextField(null=True)),
                ('interview_date', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(null=True)),
                ('current_org', models.TextField(null=True)),
                ('qualification', models.TextField(null=True)),
                ('total_exp', models.FloatField(null=True)),
                ('current_location', models.TextField(null=True)),
                ('contact_details_mobile', models.IntegerField(null=True)),
                ('contact_details_phone2', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('current_salary', models.FloatField(null=True)),
                ('expected_salary_percentage', models.IntegerField(null=True)),
                ('expected_salary_amt', models.FloatField(null=True)),
                ('notice_period', models.FloatField(null=True)),
                ('Int_Tele_Date', models.DateField(blank=True, null=True)),
                ('Int_Tele_Result', models.TextField(blank=True, null=True)),
                ('Int_P1_Date', models.DateField(blank=True, null=True)),
                ('Int_P1_Result', models.TextField(blank=True, null=True)),
                ('Int_p2_Date', models.DateField(blank=True, null=True)),
                ('Int_p2_Result', models.TextField(blank=True, null=True)),
                ('Int_p3_Date', models.DateField(blank=True, null=True)),
                ('Int_p3_Result', models.TextField(blank=True, null=True)),
                ('Int_Final_Date', models.DateField(blank=True, null=True)),
                ('Int_Final_Result', models.TextField(blank=True, null=True)),
                ('Int_HR_Date', models.DateField(blank=True, null=True)),
                ('Int_HR_Result', models.TextField(blank=True, null=True)),
                ('offer_date', models.DateField(blank=True, null=True)),
                ('offer_amt', models.FloatField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('vacancy_code', models.TextField(blank=True, null=True)),
                ('applicant_code', models.TextField(blank=True, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('preferred_company', models.TextField(blank=True, null=True)),
                ('preferred_location', models.TextField(blank=True, null=True)),
                ('week_number', models.IntegerField(blank=True, null=True)),
                ('wk_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoodRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.TextField(null=True)),
                ('reqt_date', models.DateField(null=True)),
                ('date_cv_submitted', models.DateField(null=True)),
                ('candidate_name', models.TextField(null=True)),
                ('current_status', models.IntegerField(null=True)),
                ('current_status_desc', models.TextField(null=True)),
                ('interview_date', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(null=True)),
                ('current_org', models.TextField(null=True)),
                ('qualification', models.TextField(null=True)),
                ('total_exp', models.FloatField(null=True)),
                ('current_location', models.TextField(null=True)),
                ('contact_details_mobile', models.IntegerField(null=True)),
                ('contact_details_phone2', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('current_salary', models.FloatField(null=True)),
                ('expected_salary_percentage', models.IntegerField(null=True)),
                ('expected_salary_amt', models.FloatField(null=True)),
                ('notice_period', models.FloatField(null=True)),
                ('Int_Tele_Date', models.DateField(blank=True, null=True)),
                ('Int_Tele_Result', models.TextField(blank=True, null=True)),
                ('Int_P1_Date', models.DateField(blank=True, null=True)),
                ('Int_P1_Result', models.TextField(blank=True, null=True)),
                ('Int_p2_Date', models.DateField(blank=True, null=True)),
                ('Int_p2_Result', models.TextField(blank=True, null=True)),
                ('Int_p3_Date', models.DateField(blank=True, null=True)),
                ('Int_p3_Result', models.TextField(blank=True, null=True)),
                ('Int_Final_Date', models.DateField(blank=True, null=True)),
                ('Int_Final_Result', models.TextField(blank=True, null=True)),
                ('Int_HR_Date', models.DateField(blank=True, null=True)),
                ('Int_HR_Result', models.TextField(blank=True, null=True)),
                ('offer_date', models.DateField(blank=True, null=True)),
                ('offer_amt', models.FloatField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('vacancy_code', models.TextField(blank=True, null=True)),
                ('applicant_code', models.TextField(blank=True, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('preferred_company', models.TextField(blank=True, null=True)),
                ('preferred_location', models.TextField(blank=True, null=True)),
                ('week_number', models.IntegerField(blank=True, null=True)),
                ('wk_year', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='records.client')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='BadRecords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.TextField(null=True)),
                ('reqt_date', models.DateField(null=True)),
                ('date_cv_submitted', models.DateField(null=True)),
                ('candidate_name', models.TextField(null=True)),
                ('current_status', models.IntegerField(null=True)),
                ('current_status_desc', models.TextField(null=True)),
                ('interview_date', models.DateField(blank=True, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(null=True)),
                ('current_org', models.TextField(null=True)),
                ('qualification', models.TextField(null=True)),
                ('total_exp', models.FloatField(null=True)),
                ('current_location', models.TextField(null=True)),
                ('contact_details_mobile', models.IntegerField(null=True)),
                ('contact_details_phone2', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('current_salary', models.FloatField(null=True)),
                ('expected_salary_percentage', models.IntegerField(null=True)),
                ('expected_salary_amt', models.FloatField(null=True)),
                ('notice_period', models.FloatField(null=True)),
                ('Int_Tele_Date', models.DateField(blank=True, null=True)),
                ('Int_Tele_Result', models.TextField(blank=True, null=True)),
                ('Int_P1_Date', models.DateField(blank=True, null=True)),
                ('Int_P1_Result', models.TextField(blank=True, null=True)),
                ('Int_p2_Date', models.DateField(blank=True, null=True)),
                ('Int_p2_Result', models.TextField(blank=True, null=True)),
                ('Int_p3_Date', models.DateField(blank=True, null=True)),
                ('Int_p3_Result', models.TextField(blank=True, null=True)),
                ('Int_Final_Date', models.DateField(blank=True, null=True)),
                ('Int_Final_Result', models.TextField(blank=True, null=True)),
                ('Int_HR_Date', models.DateField(blank=True, null=True)),
                ('Int_HR_Result', models.TextField(blank=True, null=True)),
                ('offer_date', models.DateField(blank=True, null=True)),
                ('offer_amt', models.FloatField(blank=True, null=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('vacancy_code', models.TextField(blank=True, null=True)),
                ('applicant_code', models.TextField(blank=True, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('preferred_company', models.TextField(blank=True, null=True)),
                ('preferred_location', models.TextField(blank=True, null=True)),
                ('week_number', models.IntegerField(blank=True, null=True)),
                ('wk_year', models.IntegerField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='records.client')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.user')),
            ],
        ),
    ]
