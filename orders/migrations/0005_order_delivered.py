# Generated by Django 3.0.6 on 2020-06-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
    ]