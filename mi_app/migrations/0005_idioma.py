# Generated by Django 4.0.5 on 2022-07-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_app', '0004_auto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=40)),
                ('conocimiento', models.CharField(max_length=40)),
            ],
        ),
    ]