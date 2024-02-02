# Generated by Django 4.0.2 on 2024-02-02 06:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0027_tab_one_model_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='tab_one_model',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tab_one_model',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
