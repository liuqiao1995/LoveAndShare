# Generated by Django 2.2.4 on 2019-09-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20190927_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(default=0, max_length=11, unique=True, verbose_name='电话'),
            preserve_default=False,
        ),
    ]