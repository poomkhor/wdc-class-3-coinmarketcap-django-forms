# Generated by Django 2.1.4 on 2019-01-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocoins', '0003_auto_20181228_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptocurrency',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
