# Generated by Django 4.2.5 on 2024-12-07 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Learn', '0008_rename_uloadskill_uploadskill'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='uploadskill',
            table='learn_skill',
        ),
    ]