# Generated by Django 5.0.2 on 2024-02-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.CharField(default='horror', max_length=100),
            preserve_default=False,
        ),
    ]
