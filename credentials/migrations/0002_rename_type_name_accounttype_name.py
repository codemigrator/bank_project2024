# Generated by Django 3.2.22 on 2024-02-08 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounttype',
            old_name='type_name',
            new_name='name',
        ),
    ]