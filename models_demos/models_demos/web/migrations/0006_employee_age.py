# Generated by Django 4.1.3 on 2022-11-02 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_employee_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=19),
            preserve_default=False,
        ),
    ]