# Generated by Django 4.2.3 on 2023-07-16 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_01', '0003_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]
