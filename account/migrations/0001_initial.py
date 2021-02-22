# Generated by Django 3.1.7 on 2021-02-22 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=254)),
                ('address2', models.CharField(blank=True, max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.PositiveIntegerField()),
                ('cust_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=254)),
                ('address1', models.CharField(max_length=254)),
                ('address2', models.CharField(blank=True, max_length=254)),
                ('city', models.CharField(max_length=254)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.PositiveIntegerField()),
                ('about', models.CharField(blank=True, max_length=999)),
                ('yr_est', models.CharField(blank=True, max_length=4, null=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='')),
                ('the_slug', models.SlugField(null=True, unique=True)),
                ('bus_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]