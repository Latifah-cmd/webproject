# Generated by Django 3.2.20 on 2023-10-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webprojects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_color', models.CharField(max_length=30)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('delievery_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
