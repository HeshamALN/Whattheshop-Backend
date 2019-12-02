# Generated by Django 2.2.7 on 2019-12-02 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartSalfa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Cart')),
                ('salfa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Salfa')),
            ],
        ),
    ]