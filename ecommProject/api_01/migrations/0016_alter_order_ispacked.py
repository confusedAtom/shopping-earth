# Generated by Django 4.2.3 on 2023-07-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_01', '0015_rename_ispaid_order_isshipped_remove_order_paidat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='isPacked',
            field=models.BooleanField(default=False),
        ),
    ]