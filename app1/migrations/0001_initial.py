# Generated by Django 4.2.7 on 2023-12-04 04:10

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('mobile_number', models.CharField(max_length=20, null=True)),
                ('profile_image', models.ImageField(null=True, upload_to='static/images/')),
                ('profile_summary', models.TextField(max_length=300, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('route', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
