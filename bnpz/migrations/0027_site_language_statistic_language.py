# Generated by Django 5.0.6 on 2024-08-21 08:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0026_statistic_titleadd'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bnpz.language', verbose_name='Tilni tanlang'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statistic',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bnpz.language', verbose_name='Tilni tanlang'),
            preserve_default=False,
        ),
    ]
