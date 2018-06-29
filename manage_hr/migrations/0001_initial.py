# Generated by Django 2.0 on 2018-06-27 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('gender', models.CharField(db_column='Gender', max_length=10)),
                ('date_of_join', models.DateTimeField()),
                ('emp_type', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('email', models.CharField(max_length=25)),
            ],
            options={
                'managed': False,
                'db_table': 'employee',
            },
        ),
    ]