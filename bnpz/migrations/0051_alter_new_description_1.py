# Generated by Django 5.0.6 on 2024-09-25 09:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0050_alter_new_description_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='description_1',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name="Ta'rif 2"),
        ),
    ]
