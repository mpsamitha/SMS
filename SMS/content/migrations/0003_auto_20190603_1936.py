# Generated by Django 2.1.7 on 2019-06-03 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20190603_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_id',
            field=models.CharField(error_messages={'unique': 'This Subject ID has already been registered.'}, max_length=20, unique=True),
        ),
    ]
