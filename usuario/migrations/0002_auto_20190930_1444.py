# Generated by Django 2.2.5 on 2019-09-30 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instituicao',
            name='senha',
        ),
        migrations.AlterField(
            model_name='instituicao',
            name='password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]