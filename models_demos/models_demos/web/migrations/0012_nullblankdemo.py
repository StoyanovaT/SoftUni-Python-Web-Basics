# Generated by Django 4.1.3 on 2022-11-02 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_employee_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='NullBlankDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blank', models.IntegerField(blank=True)),
                ('null', models.IntegerField(null=True)),
                ('blank_null', models.IntegerField(blank=True, null=True)),
                ('default', models.IntegerField()),
            ],
        ),
    ]
