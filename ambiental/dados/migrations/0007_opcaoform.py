# Generated by Django 2.1.3 on 2018-11-27 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0006_tanque'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpcaoForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('possui_contrucao', models.TextField()),
                ('tela', models.TextField()),
                ('wetlands', models.TextField()),
            ],
        ),
    ]