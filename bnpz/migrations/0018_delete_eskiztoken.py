# Generated by Django 5.0.6 on 2024-08-16 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0017_rename_token_eskiztoken'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EskizToken',
        ),
    ]
