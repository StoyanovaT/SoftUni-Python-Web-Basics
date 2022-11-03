# Generated by Django 4.1.3 on 2022-11-03 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_accesscard_alter_employee_projects_employeesprojects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='web.category')),
            ],
        ),
    ]
