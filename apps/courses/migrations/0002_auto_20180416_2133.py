# Generated by Django 2.0.3 on 2018-04-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(choices=[('cj', '初级'), ('zj', '中极'), ('gj', '高级')], max_length=2, verbose_name='等级'),
        ),
    ]
