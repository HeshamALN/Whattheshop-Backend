# Generated by Django 2.2.7 on 2019-12-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_cartsalfa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='salfa',
            field=models.ManyToManyField(through='api.CartSalfa', to='api.Salfa'),
        ),
    ]
