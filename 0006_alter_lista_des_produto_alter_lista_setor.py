# Generated by Django 5.1.4 on 2025-01-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_lista_delete_testes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='des_produto',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lista',
            name='setor',
            field=models.CharField(max_length=255),
        ),
    ]
