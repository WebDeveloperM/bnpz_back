# Generated by Django 5.0.6 on 2024-08-28 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0040_lider_alter_localdocs_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='lider',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bnpz.language', verbose_name='Tilni tanlang'),
            preserve_default=False,
        ),
    ]
