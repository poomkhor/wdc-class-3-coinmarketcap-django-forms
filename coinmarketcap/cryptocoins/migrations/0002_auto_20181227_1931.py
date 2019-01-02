# Generated by Django 2.1.4 on 2018-12-27 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocoins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(blank=True, max_length=1200)),
            ],
        ),
        migrations.AddField(
            model_name='cryptocurrency',
            name='exchange',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='cryptocoins.Exchange'),
            preserve_default=False,
        ),
    ]