# Generated by Django 3.1.5 on 2021-02-18 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20210212_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]