# Generated by Django 2.1.7 on 2019-06-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20190603_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='address',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='user_address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]