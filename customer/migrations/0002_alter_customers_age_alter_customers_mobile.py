# Generated by Django 4.2.1 on 2023-05-15 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
