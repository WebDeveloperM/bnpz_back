# Generated by Django 5.0.6 on 2024-08-22 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0027_site_language_statistic_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorytender',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bnpz.language', verbose_name='Tilni tanlang'),
            preserve_default=False,
        ),
    ]
