# Generated by Django 5.0.3 on 2024-03-19 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utilitiesapp', '0011_rename_resolveddatetime_services_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='services',
            name='updated_at',
        ),
    ]
