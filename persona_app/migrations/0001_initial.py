# Generated by Django 4.0 on 2021-12-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('address_street', models.CharField(max_length=128)),
                ('address_number', models.IntegerField()),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=32)),
                ('postcode', models.CharField(max_length=6)),
                ('email', models.CharField(max_length=128)),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('age', models.IntegerField()),
                ('picture', models.CharField(max_length=4096)),
            ],
        ),
    ]
