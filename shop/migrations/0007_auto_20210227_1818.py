# Generated by Django 3.1.7 on 2021-02-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210226_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(blank=True, to='shop.CartProduct'),
        ),
    ]
