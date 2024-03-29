# Generated by Django 4.1.7 on 2023-04-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_order_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='currency',
            field=models.CharField(choices=[('UZS', 'UZS'), ('RUB', 'RUB'), ('USD', 'USD')], max_length=9),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('CASH', 'CASH'), ('BANK CARD', 'BANK CARD'), ('TRANSFER', 'TRANSFER')], max_length=9),
        ),
    ]
