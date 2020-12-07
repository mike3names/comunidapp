# Generated by Django 3.1.2 on 2020-12-07 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_auto_20201207_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='palabras_clave',
            field=models.ManyToManyField(blank=True, to='Users.PalabrasClave'),
        ),
        migrations.AlterField(
            model_name='capitulolibro',
            name='palabras_clave',
            field=models.ManyToManyField(blank=True, to='Users.PalabrasClave'),
        ),
        migrations.AlterField(
            model_name='congreso',
            name='palabras_clave',
            field=models.ManyToManyField(blank=True, to='Users.PalabrasClave'),
        ),
        migrations.AlterField(
            model_name='investigacion',
            name='palabras_clave',
            field=models.ManyToManyField(blank=True, to='Users.PalabrasClave'),
        ),
        migrations.AlterField(
            model_name='tesis',
            name='palabras_clave',
            field=models.ManyToManyField(blank=True, to='Users.PalabrasClave'),
        ),
    ]
