# Generated by Django 5.2.1 on 2025-06-26 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0002_livro_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='livro',
            name='publicado',
            field=models.BooleanField(default=False),
        ),
    ]
