# Generated by Django 4.1.6 on 2023-02-13 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_currency_alter_order_payment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='unit_price',
        ),
    ]