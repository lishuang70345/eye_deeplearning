# Generated by Django 3.1.7 on 2021-08-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyetest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='photoOD_result',
            field=models.URLField(default='', verbose_name='右眼照片结果'),
        ),
        migrations.AddField(
            model_name='info',
            name='photoOS_result',
            field=models.URLField(default='', verbose_name='左眼照片结果'),
        ),
    ]
