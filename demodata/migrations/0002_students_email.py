# Generated by Django 2.2.1 on 2020-02-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demodata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='邮箱'),
        ),
    ]
