# Generated by Django 3.2.14 on 2022-07-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pull_users_api', '0003_alter_users_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m', max_length=1),
        ),
    ]
