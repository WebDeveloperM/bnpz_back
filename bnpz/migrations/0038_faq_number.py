# Generated by Django 5.0.6 on 2024-08-26 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0037_alter_categorytender_options_selection_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Nomer'),
            preserve_default=False,
        ),
    ]
