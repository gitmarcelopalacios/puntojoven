# Generated by Django 4.0.4 on 2022-05-10 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='idestudiante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='estudiante.estudiante'),
            preserve_default=False,
        ),
    ]