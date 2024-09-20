# Generated by Django 5.0.6 on 2024-08-28 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bnpz', '0038_faq_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalDocs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Hujjat nomi')),
                ('file', models.FileField(upload_to='', verbose_name='Fayl')),
            ],
            options={
                'verbose_name': 'LocalDocs',
                'verbose_name_plural': "10. Lokal me'yoriy hujjatlar",
            },
        ),
    ]
