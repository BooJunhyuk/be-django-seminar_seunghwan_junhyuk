# Generated by Django 4.2 on 2023-05-06 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_post_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='headline',
            field=models.CharField(max_length=200, verbose_name='제목'),
        ),
    ]
