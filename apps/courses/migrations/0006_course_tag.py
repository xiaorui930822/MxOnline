# Generated by Django 2.0.3 on 2018-05-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=50, verbose_name='课程标签'),
        ),
    ]
