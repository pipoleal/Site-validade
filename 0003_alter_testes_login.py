# Generated by Django 5.1.4 on 2024-12-24 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_testes_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testes',
            name='login',
            field=models.TextField(max_length=255),
        ),
    ]
