# Generated by Django 4.1.5 on 2024-02-02 14:02

import django.core.validators
from django.db import migrations, models
import form1.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tab_one_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digit', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10000000)])),
                ('name', models.TextField(default='none')),
                ('country', models.TextField(null=True)),
                ('ratings', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)])),
                ('date', models.DateField(blank=True, null=True)),
                ('city', models.CharField(choices=[('none', 'None'), ('Delhi', 'Delhi'), ('Gurgaon', 'Gurgaon'), ('Bangalore', 'Bangalore')], default='none', max_length=20, null=True)),
                ('color', models.CharField(choices=[('none', 'None'), ('red', 'Red'), ('green', 'Green'), ('blue', 'Blue')], default='none', max_length=5, null=True)),
                ('check1', models.BooleanField(default=False)),
                ('check2', models.BooleanField(default=False)),
                ('check3', models.BooleanField(default=False)),
                ('describe', models.CharField(default='none', max_length=100)),
                ('asdf', models.IntegerField()),
                ('website', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(message="Enter a valid domain name (e.g., 'example.com').", regex='^[a-zA-Z0-9-]+(\\.[a-zA-Z0-9-]+)+$'), form1.models.validate_domain_name])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(default='2021-02-01 00:00:00')),
            ],
        ),
    ]
