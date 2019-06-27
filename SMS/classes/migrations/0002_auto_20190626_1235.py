# Generated by Django 2.1.7 on 2019-06-26 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classes',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classes',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
