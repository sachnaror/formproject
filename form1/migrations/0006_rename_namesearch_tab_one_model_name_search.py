# Generated by Django 4.0.2 on 2024-02-03 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0005_tab_one_model_namesearch'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tab_one_model',
            old_name='namesearch',
            new_name='name_search',
        ),
    ]