# Generated by Django 3.0.4 on 2020-05-26 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('turistikmekan', '0017_product_guidecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='turistikmekan.Category'),
            preserve_default=False,
        ),
    ]
