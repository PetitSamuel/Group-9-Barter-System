# Generated by Django 3.1.3 on 2021-03-12 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.SlugField(max_length=32, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=80, null=True)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('isBusiness', models.BooleanField(default=False)),
                ('bio', models.TextField()),
            ],
        ),
    ]
