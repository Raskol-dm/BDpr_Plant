# Generated by Django 3.0.7 on 2022-08-25 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20220825_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='name',
            new_name='rname',
        ),
    ]
