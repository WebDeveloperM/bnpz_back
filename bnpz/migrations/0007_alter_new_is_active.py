# Generated by Django 5.0.6 on 2024-08-14 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0006_alter_new_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Active:'),
        ),
    ]
