# Generated by Django 3.1.7 on 2021-09-17 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-id',)},
        ),
    ]
