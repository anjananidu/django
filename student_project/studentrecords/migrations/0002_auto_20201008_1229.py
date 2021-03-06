# Generated by Django 3.1.1 on 2020-10-08 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentrecords', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='Reg_no',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stud_phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
