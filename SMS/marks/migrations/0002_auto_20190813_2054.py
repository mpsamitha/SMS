# Generated by Django 2.1.7 on 2019-08-13 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='marks1',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks10',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks2',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks3',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks4',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks5',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks6',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks7',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks8',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='marks9',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject1', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject10',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject10', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject2', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject3',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject3', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject4',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject4', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject5',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject5', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject6',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject6', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject7',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject7', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject8',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject8', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject9',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject9', to='content.Subject'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='total',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
    ]
