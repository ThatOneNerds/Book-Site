# Generated by Django 3.2.9 on 2022-05-26 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220526_0313'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='books',
            new_name='book',
        ),
    ]
