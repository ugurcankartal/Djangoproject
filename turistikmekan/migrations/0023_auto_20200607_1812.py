# Generated by Django 3.0.4 on 2020-06-07 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistikmekan', '0022_auto_20200607_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='status',
            field=models.CharField(blank=True, choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10),
        ),
    ]
