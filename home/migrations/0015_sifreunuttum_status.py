# Generated by Django 3.0.4 on 2020-06-11 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200611_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='sifreunuttum',
            name='status',
            field=models.CharField(blank=True, choices=[('Gonderildi', 'Gonderildi'), ('Gonderilmedi', 'Gonderilmedi')], max_length=20),
        ),
    ]
