# Generated by Django 5.0.6 on 2024-09-25 09:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0053_alter_new_description_2_alter_new_description_3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='description_1',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name="Ta'rif 1"),
        ),
    ]
