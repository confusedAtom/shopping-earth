# Generated by Django 4.2.3 on 2023-07-21 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_01', '0014_delete_shippingaddress'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='isPaid',
            new_name='isShipped',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paidAt',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paymentMethod',
        ),
        migrations.AddField(
            model_name='order',
            name='isPacked',
            field=models.BooleanField(default=True),
        ),
    ]
