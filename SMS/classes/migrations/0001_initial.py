# Generated by Django 2.1.7 on 2019-08-13 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_no', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=20)),
                ('class_grade', models.CharField(choices=[('GRADE 1', 'GRADE 1'), ('GRADE 2', 'GRADE 2'), ('GRADE 3', 'GRADE 3'), ('GRADE 4', 'GRADE 4'), ('GRADE 5', 'GRADE 5'), ('GRADE 6', 'GRADE 6'), ('GRADE 7', 'GRADE 7'), ('GRADE 8', 'GRADE 8'), ('GRADE 9', 'GRADE 9'), ('GRADE 10', 'GRADE 10'), ('GRADE 11', 'GRADE 11')], default='GRADE 10', max_length=20)),
            ],
            options={
                'db_table': 'classes',
            },
        ),
        migrations.AlterUniqueTogether(
            name='classes',
            unique_together={('class_no', 'class_grade')},
        ),
        migrations.AddField(
            model_name='classdetails',
            name='classes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Classes'),
        ),
        migrations.AddField(
            model_name='classdetails',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='classdetails',
            name='teacher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]
