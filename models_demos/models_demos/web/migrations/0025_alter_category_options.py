# Generated by Django 4.1.3 on 2022-11-10 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_alter_employee_options_department_created_on_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
