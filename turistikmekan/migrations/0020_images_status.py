# Generated by Django 3.0.4 on 2020-06-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turistikmekan', '0019_remove_product_guidecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='status',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
