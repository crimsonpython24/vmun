# Generated by Django 3.1 on 2020-11-10 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201108_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday_vis',
            field=models.BooleanField(blank=True, default=False, verbose_name='birthday visibility'),
        ),
        migrations.AddField(
            model_name='user',
            name='email_vis',
            field=models.BooleanField(blank=True, default=False, verbose_name='email visibility'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender_vis',
            field=models.BooleanField(blank=True, default=False, verbose_name='gender visibility'),
        ),
        migrations.AddField(
            model_name='user',
            name='intro_vis',
            field=models.BooleanField(blank=True, default=False, verbose_name='introduction visibility'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname_vis',
            field=models.BooleanField(blank=True, default=False, verbose_name='nickname visibility'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_vis',
            field=models.BooleanField(blank=True, default=False, verbose_name='phone visibility'),
        ),
    ]