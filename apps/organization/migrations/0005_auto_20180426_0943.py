# Generated by Django 2.0.3 on 2018-04-26 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_teacher_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='头像'),
        ),
    ]