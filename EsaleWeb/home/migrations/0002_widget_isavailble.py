# Generated by Django 4.0.5 on 2022-07-01 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='widget',
            name='isAvailble',
            field=models.BooleanField(null=True),
        ),
    ]
