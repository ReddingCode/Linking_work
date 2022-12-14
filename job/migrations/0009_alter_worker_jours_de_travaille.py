# Generated by Django 3.2.16 on 2022-10-30 10:51

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_alter_worker_jours_de_travaille'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='jours_de_travaille',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('LUNDI', 'LUNDI'), ('MARDI', 'MARDI'), ('MERCREDI', 'MERCREDI'), ('JEUDI', 'JEUDI'), ('VENDREDI', 'VENDREDI'), ('DIMANCHE', 'DIMANCHE'), ('DIMANCHE', 'DIMANCHE')], max_length=53),
        ),
    ]
