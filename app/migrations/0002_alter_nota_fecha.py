# Generated by Django 3.2.5 on 2021-07-07 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='fecha',
            field=models.DateField(),
        ),
    ]
