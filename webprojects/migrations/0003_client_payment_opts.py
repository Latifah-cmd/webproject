# Generated by Django 3.2.20 on 2023-10-31 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webprojects', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='payment_opts',
            field=models.CharField(choices=[('MM', 'mobilemoney'), ('VC', 'visacard'), ('CD', 'cashondelievery')], default=0, max_length=15),
            preserve_default=False,
        ),
    ]
