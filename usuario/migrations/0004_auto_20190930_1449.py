# Generated by Django 2.2.5 on 2019-09-30 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_instituicao_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instituicao',
            name='is_staff',
            field=models.NullBooleanField(default=True),
        ),
    ]
