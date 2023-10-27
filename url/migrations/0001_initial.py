# Generated by Django 4.2.6 on 2023-10-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=2048)),
                ('short_code', models.UUIDField(unique=True)),
            ],
        ),
    ]