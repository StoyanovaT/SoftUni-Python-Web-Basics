# Generated by Django 4.1.3 on 2022-11-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_nullblankdemo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_full_time',
            field=models.BooleanField(null=True),
        ),
    ]
