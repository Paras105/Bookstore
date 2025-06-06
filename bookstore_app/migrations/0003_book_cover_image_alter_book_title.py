# Generated by Django 5.2 on 2025-04-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore_app', '0002_remove_book_description_remove_book_published_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.URLField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
