# Generated by Django 3.1.1 on 2020-10-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentrecords', '0002_auto_20201008_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg_no', models.CharField(max_length=20, unique=True)),
                ('stud_name', models.CharField(max_length=100)),
                ('stud_email', models.EmailField(max_length=254, unique=True)),
                ('stud_phone', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
