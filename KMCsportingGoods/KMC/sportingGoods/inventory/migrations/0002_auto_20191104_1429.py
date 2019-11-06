# Generated by Django 2.2.6 on 2019-11-04 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='vender',
            new_name='vendor',
        ),
        migrations.AlterField(
            model_name='inventory',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterUniqueTogether(
            name='inventory',
            unique_together={('product', 'vendor', 'color')},
        ),
    ]