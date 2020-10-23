# Generated by Django 3.1 on 2020-10-23 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200)),
                ('chair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=200, unique=True)),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Delegate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('nation', models.CharField(max_length=100)),
                ('committee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mun.committee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='committee',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mun.conference'),
        ),
    ]