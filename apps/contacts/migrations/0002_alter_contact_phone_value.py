# Generated by Django 4.0.5 on 2022-07-03 07:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone_value',
            field=models.PositiveBigIntegerField(help_text='Phone number of contact', verbose_name='Phone number'),
        ),
    ]
