# Generated by Django 3.1.1 on 2020-10-08 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentrecords', '0003_auto_20201008_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='id',
        ),
        migrations.AlterField(
            model_name='students',
            name='Reg_no',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]