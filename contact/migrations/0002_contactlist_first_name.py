# Generated by Django 2.2.13 on 2021-01-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactlist',
            name='first_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]