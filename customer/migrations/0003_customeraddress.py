# Generated by Django 4.2.1 on 2023-05-25 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_customers_age_alter_customers_mobile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_name', models.CharField(blank=True, max_length=15, null=True)),
                ('street_number', models.IntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('pincode', models.IntegerField(blank=True, null=True)),
                ('Customers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customers')),
            ],
        ),
    ]
