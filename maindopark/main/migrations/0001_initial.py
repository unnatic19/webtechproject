# Generated by Django 2.1.7 on 2019-04-21 17:09

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
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(default='', max_length=7)),
                ('country_name', models.CharField(default='', max_length=7)),
                ('car_rides', models.IntegerField(default=0)),
                ('phone_number', models.IntegerField(default=0)),
                ('email', models.EmailField(default='', max_length=254)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
