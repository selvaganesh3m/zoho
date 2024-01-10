# Generated by Django 5.0 on 2024-01-10 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_produtionorderinvoice_invoice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesorderinvoice',
            name='order',
        ),
        migrations.AddField(
            model_name='productionorder',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='production-invoices/'),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='sales-invoices/'),
        ),
        migrations.DeleteModel(
            name='ProdutionOrderInvoice',
        ),
        migrations.DeleteModel(
            name='SalesOrderInvoice',
        ),
    ]