# Generated by Django 3.1.2 on 2020-11-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20201114_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='isnn',
            field=models.CharField(max_length=13),
        ),
    ]