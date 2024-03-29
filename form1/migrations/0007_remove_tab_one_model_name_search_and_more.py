# Generated by Django 4.0.2 on 2024-02-03 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form1', '0006_rename_namesearch_tab_one_model_name_search'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tab_one_model',
            name='name_search',
        ),
        migrations.RemoveField(
            model_name='tab_one_model',
            name='tem',
        ),
        migrations.AddField(
            model_name='tab_one_model',
            name='user_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='tab_one_model',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default='2021-02-01 00:00:00'),
        ),
    ]
