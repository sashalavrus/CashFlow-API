# Generated by Django 2.2.13 on 2020-08-19 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('costs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['pub_date']},
        ),
    ]
