# Generated by Django 4.1.3 on 2022-11-02 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_alter_employee_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=-7),
        ),
    ]