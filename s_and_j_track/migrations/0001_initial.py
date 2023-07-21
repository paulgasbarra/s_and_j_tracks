# Generated by Django 4.2.3 on 2023-07-21 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField()),
                ('website', models.URLField()),
                ('instagram', models.URLField()),
                ('tiktok', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('website', models.URLField()),
                ('primary_contact', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField()),
                ('job_listings', models.URLField()),
                ('company_size', models.IntegerField()),
                ('speciality', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('linkedin', models.URLField()),
                ('resume_link', models.URLField()),
                ('lca_cert', models.BooleanField(default=False)),
                ('epa_608_cert', models.BooleanField(default=False)),
                ('s_j_cert', models.BooleanField(default=False)),
                ('class_site', models.CharField(max_length=200)),
                ('class_number', models.IntegerField()),
                ('class_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateField()),
                ('passed_date', models.DateField(blank=True, null=True)),
                ('hired_date', models.DateField(blank=True, null=True)),
                ('salary_or_hourly_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_and_j_track.employer')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_and_j_track.student')),
            ],
        ),
    ]
