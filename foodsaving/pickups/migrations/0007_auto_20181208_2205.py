# Generated by Django 2.1.2 on 2018-12-08 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pickups', '0006_auto_20181207_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickupdate',
            old_name='deleted',
            new_name='is_cancelled',
        ),
        migrations.RemoveField(
            model_name='pickupdate',
            name='cancelled_at',
        ),
    ]
