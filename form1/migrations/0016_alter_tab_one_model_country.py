# Generated by Django 4.0.2 on 2024-01-29 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0015_alter_tab_one_model_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tab_one_model',
            name='country',
            field=models.TextField(null=True),
        ),
    ]