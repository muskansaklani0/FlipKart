# Generated by Django 4.2.1 on 2023-05-27 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_customer_addhar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_iriksha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(blank=True, max_length=15, null=True)),
                ('Customer_no', models.IntegerField(blank=True, null=True)),
                ('Customers', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customers')),
            ],
        ),
    ]