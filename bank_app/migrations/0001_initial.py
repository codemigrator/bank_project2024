# Generated by Django 3.2.22 on 2024-02-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches_Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=70, unique=True)),
                ('link', models.TextField(unique=True)),
            ],
        ),
    ]
