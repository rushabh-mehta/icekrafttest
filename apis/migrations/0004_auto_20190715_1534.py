# Generated by Django 2.2.2 on 2019-07-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20190715_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]