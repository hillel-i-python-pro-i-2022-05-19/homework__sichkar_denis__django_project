# Generated by Django 4.0.6 on 2022-07-10 07:02

import django.core.validators
import django.db.models.deletion
import multiselectfield.db.fields
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contacts', '0008_delete_tagschoices_remove_contact_contact_tag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='LinkedinURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin', models.CharField(max_length=30, unique=True, validators=[
                    django.core.validators.URLValidator(
                        message='Enter a link starting with "https://www.linkedin.com/in/"',
                        schemes=['https://www.linkedin.com/in/'])], verbose_name='Linkedin URL')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone',
                 phonenumber_field.modelfields.PhoneNumberField(help_text='Phone number of contact', max_length=13,
                                                                region=None, unique=True, verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='TelegramNickname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram', models.SlugField(max_length=20, unique=True, verbose_name='Telegram')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_tags',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('FAMILY', 'Family'), ('JOB', 'Job'),
                                                                                   ('FRIENDS', 'Friends'),
                                                                                   ('JOURNEY', 'Journey'),
                                                                                   ('EVENT', 'Event'),
                                                                                   ('UNIVERSITY', 'University')],
                                                              help_text='Contact Tags', max_length=43, null=True,
                                                              verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_email',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='contacts.email'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_linkedin',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                       to='contacts.linkedinurl'),
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_telegram',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                       to='contacts.telegramnickname'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_value',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                       to='contacts.phonenumber'),
        ),
    ]