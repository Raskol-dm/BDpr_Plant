# Generated by Django 3.2.15 on 2022-09-17 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220825_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watrlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('upwaterfreq', models.DateField(auto_now=True)),
                ('nextwaterfreq', models.DateField(auto_now=True)),
                ('pname_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.plants')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.room')),
            ],
            options={
                'verbose_name': 'Журнал полива',
                'verbose_name_plural': 'Журнал поливов',
                'ordering': ('room_id',),
            },
        ),
    ]
