# Generated by Django 4.1.2 on 2022-12-05 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_comment_content_alter_comment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
