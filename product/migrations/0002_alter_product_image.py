# Generated by Django 5.0.1 on 2024-02-11 18:40

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True, null=True, upload_to="images/testimagemodel/"
            ),
        ),
    ]
