# Generated by Django 5.2.1 on 2025-06-05 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authory', '0002_rename_email_code_email_code_emailcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email_code',
            old_name='emailcode',
            new_name='email_code',
        ),
    ]
