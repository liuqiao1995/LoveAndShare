# Generated by Django 2.2.4 on 2019-10-13 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20191012_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='电话'),
        ),
    ]
