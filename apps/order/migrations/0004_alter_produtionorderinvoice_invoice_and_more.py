# Generated by Django 5.0 on 2024-01-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_produtionorderinvoice_salesorderinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtionorderinvoice',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='invoices/'),
        ),
        migrations.AlterField(
            model_name='salesorderinvoice',
            name='invoice',
            field=models.FileField(blank=True, null=True, upload_to='invoices/'),
        ),
    ]
