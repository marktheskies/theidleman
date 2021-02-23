# Generated by Django 3.1.5 on 2021-02-23 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_productcategory_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_reference',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='productadditionalimage',
            name='reference',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='core.productcategory'),
        ),
    ]
