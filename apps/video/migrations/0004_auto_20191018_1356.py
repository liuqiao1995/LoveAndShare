# Generated by Django 2.2.4 on 2019-10-18 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20191018_1354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='img_url',
        ),
        migrations.AddField(
            model_name='course',
            name='img',
            field=models.FileField(default='', upload_to='video_img/', verbose_name='图片'),
        ),
    ]