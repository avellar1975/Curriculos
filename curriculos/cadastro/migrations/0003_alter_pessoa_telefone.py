# Generated by Django 3.2 on 2021-04-22 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_pessoa_formacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(default='(00)000-000-000', max_length=20),
        ),
    ]
