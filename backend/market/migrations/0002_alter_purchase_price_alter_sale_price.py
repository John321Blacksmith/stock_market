# Generated by Django 4.2.2 on 2023-06-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=14, null=True),
        ),
    ]