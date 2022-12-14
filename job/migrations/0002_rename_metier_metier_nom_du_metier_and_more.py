# Generated by Django 4.1 on 2022-10-14 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metier',
            old_name='metier',
            new_name='nom_du_metier',
        ),
        migrations.RemoveField(
            model_name='metier',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='metier',
            name='worker',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='slug',
        ),
        migrations.AlterField(
            model_name='worker',
            name='metier',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='job.metier'),
        ),
    ]
