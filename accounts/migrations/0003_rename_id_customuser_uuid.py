# Generated by Django 4.2.3 on 2023-07-29 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='id',
            new_name='uuid',
        ),
    ]