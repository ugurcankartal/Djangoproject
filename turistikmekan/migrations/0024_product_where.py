# Generated by Django 3.0.4 on 2020-06-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistikmekan', '0023_auto_20200607_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='where',
            field=models.CharField(blank=True, choices=[('Yurtici', 'Yurt içi'), ('Yurtdisi', 'Yurd Dışı')], max_length=15),
        ),
    ]
