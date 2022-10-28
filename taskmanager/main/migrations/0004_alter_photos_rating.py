# Generated by Django 4.1.2 on 2022-10-27 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_photos_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, default=0.0, max_digits=2),
        ),
    ]
