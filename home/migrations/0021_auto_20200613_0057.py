# Generated by Django 3.0.4 on 2020-06-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_sifreunuttum_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sifreunuttum',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
