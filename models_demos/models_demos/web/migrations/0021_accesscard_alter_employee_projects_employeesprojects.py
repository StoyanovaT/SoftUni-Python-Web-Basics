# Generated by Django 4.1.3 on 2022-11-03 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0020_project_employee_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCard',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.employee')),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='projects',
            field=models.ManyToManyField(related_name='employees', to='web.project'),
        ),
        migrations.CreateModel(
            name='EmployeesProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.employee')),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.project')),
            ],
        ),
    ]
