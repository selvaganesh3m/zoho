# Generated by Django 5.0 on 2024-01-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_remove_salesorderinvoice_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='status',
            field=models.CharField(choices=[('ORDER_RECIEVED', 'ORDER RECIEVED'), ('ORDER_PROCESSING', 'ORDER PROCESSING'), ('ORDER_COMPLETED', 'ORDER_COMPLETED'), ('INVOICE_ISSUED', 'INVOICE ISSUED')], default='ORDER_RECIEVED', max_length=30),
        ),
    ]