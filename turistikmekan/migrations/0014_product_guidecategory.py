# Generated by Django 3.0.4 on 2020-05-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistikmekan', '0013_auto_20200526_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='guidecategory',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
