# Generated by Django 4.1.2 on 2022-10-31 17:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ish', models.CharField(max_length=200)),
                ('rot', models.IntegerField(max_length=200)),
                ('zac', models.CharField(max_length=200)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
